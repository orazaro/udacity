import os
import re
import sys
import urllib2
from xml.dom import minidom
from string import letters

import webapp2
import jinja2

from google.appengine.ext import db


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BlogHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

def render_post(response, post):
    response.out.write('<b>' + post.subject + '</b><br>')
    response.out.write(post.content)

def make_secure_val(s):
    import hmac
    SECRET = 'bigS'
    def hash_str(s):
        #return hashlib.md5(s).hexdigest()
        return hmac.new(SECRET,s).hexdigest()
    return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    s = h.split('|')[0]
    return s if h==make_secure_val(s) else None

# Google maps
GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false&"
def gmap_img(points):
    markers = '&'.join('markers=%s,%s' % (p.lat, p.lon) for p in points)
    return GMAPS_URL + markers

# Hostip
IP_URL = "http://api.hostip.info/?ip="
def get_coords(ip):
    #ip = "81.19.70.3"
    url = IP_URL + ip
    content = None
    try:
        content = urllib2.urlopen(url).read()
    except URLError:
        return

    if content:
        d = minidom.parseString(content)
        coords = d.getElementsByTagName("gml:coordinates")
        if coords and coords[0].childNodes[0].nodeValue:
            lon, lat = coords[0].childNodes[0].nodeValue.split(',')
            return db.GeoPt(lat, lon)

class MainPage(BlogHandler):
  def get(self):
    #self.response.headers['Content-Type'] = 'text/plain'
    visits = 0
    cookie_visits = self.request.cookies.get('visits')
    if cookie_visits:
        v = check_secure_val(cookie_visits)
        if v:
            visits = int(v)
    visits += 1
    set_visits = make_secure_val(str(visits))
    self.response.headers.add_header('Set-Cookie','visits=%s' % set_visits)
    self.write('Hello, you\'ve made %s visits!' % str(visits))
    self.write('<br>Your ip: %s' % (self.request.remote_addr))
    # out google map
    points = []
    coords = get_coords('4.2.2.2')
    if coords: points.append(coords)
    coords = get_coords(self.request.remote_addr)
    if coords: points.append(coords)
    img_url = gmap_img(points)
    self.write('<p><img  class="map" src="'+img_url+'">')


##### blog stuff

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self)

class BlogFront(BlogHandler):
    def get(self):
        start = self.request.get('start')
        if not start: 
            start = 0
        else:
            start = int(start)
        p = "select * from Post order by created desc limit %d,10" % (start)
        posts = db.GqlQuery(p)
        start += 10
        self.render('front.html', posts = posts, start=start)

class PostPage(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return

        self.render("permalink.html", post = post)

class NewPost(BlogHandler):
    def get(self):
        self.render("newpost.html")

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(parent = blog_key(), subject = subject, content = content)
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content, error=error)



###### user stuff

import secret

class User(db.Model):
    name = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    email = db.StringProperty(required = False)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    def render(self):
        return render_str("user.html", p = self)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class Signup(BlogHandler):

    def get(self):
        self.render("signup-form.html")

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username = username,
                      email = email)

        if not valid_username(username):
            params['error_username'] = "That's not a valid username."
            have_error = True
        else:
            users = db.GqlQuery('select * from User where name=:1',username)
            if users.count() > 0:
                params['error_username'] = "This user already exists."
                have_error = True

        if not valid_password(password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif password != verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if not valid_email(email):
            params['error_email'] = "That's not a valid email."
            have_error = True

        if have_error:
            self.render('signup-form.html', **params)
            return
        # save this user
        pw = secret.make_pw_hash(username, password)
        udic = dict(name=username,password = pw)
        if email:
            udic['email'] = email
        u = User(**udic)
        u.put()
        user_id = u.key().id()
        set_user_id = make_secure_val(str(user_id))
        self.response.headers.add_header('Set-Cookie','user_id=%s' % set_user_id)
        self.redirect('/welcome')

class Login(BlogHandler):

    def get(self):
        self.render("login-form.html")

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')

        params = dict(username = username)

        if not valid_username(username):
            params['error_login'] = "Login error."
            have_error = True
        if not valid_password(password):
            params['error_login'] = "Login error."
            have_error = True
        if have_error:
            self.render('login-form.html', **params)
            return

        users = db.GqlQuery('select * from User where name=:1',username)
        if users.count() == 0:
            params['error_login'] = "Login error."
            have_error = True
        elif users.count() != 1:
            params['error_login'] = "Internal error."
            have_error = True
        elif not secret.valid_pw(username,password,users[0].password):
            params['error_login'] = "Login error."
            have_error = True
        if have_error:
            self.render('login-form.html', **params)
            return

        user_id = users[0].key().id()
        set_user_id = make_secure_val(str(user_id))
        self.response.headers.add_header('Set-Cookie','user_id=%s; Path=/' % set_user_id)
        self.redirect('/welcome')

class Welcome(BlogHandler):
    def get_user_id(self):
        user_id = None
        cookie_user_id = self.request.cookies.get('user_id')
        if cookie_user_id:
            id = check_secure_val(cookie_user_id)
            if id:
                user_id = int(id)
        return user_id
    def get(self):
        user_id = self.get_user_id()
        if user_id:
            u = User.get_by_id(user_id)
            if u:
                username = u.name
            else:
                username = user_id
            self.render('welcome.html', username = username)
        else:
            self.redirect('/signup')

class Logout(BlogHandler):
    def get(self):
        self.response.headers.add_header('Set-Cookie','user_id=%s; Path=/' % '')
        self.redirect('/signup')

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/signup', Signup),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/welcome', Welcome),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ],
                              debug=True)

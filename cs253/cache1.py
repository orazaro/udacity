import time

# complex_computation() simulates a slow function. time.sleep(n) causes the
# program to pause for n seconds. In real life, this might be a call to a
# database, or a request to another web service.
def complex_computation(a, b):
    time.sleep(.5)
    return a + b

# QUIZ - Improve the cached_computation() function below so that it caches
# results after computing them for the first time so future calls are faster
cache = {}
def cached_computation(a, b):
    ###Your code here.
    if (a,b) in cache:
        r = cache[(a,b)]
    else:
        r = complex_computation(a,b)
        cache[(a,b)] = r
    return r

def cached_computation2(a, b):
    ###Your code here.
    try:
        r = cache[(a,b)]
    except:
        r = complex_computation(a,b)
        cache[(a,b)] = r
    return r

start_time = time.time()
print cached_computation(5, 3)
print "the first computation took %f seconds" % (time.time() - start_time)

n = 10000000
start_time2 = time.time()
for _ in range(n):
    cached_computation(5, 3)
dt = float(time.time() - start_time2)/n
print "the second computation took %3.8lf seconds" % dt
start_time2 = time.time()
for _ in range(n):
    cached_computation2(5, 3)
dt = float(time.time() - start_time2)/n
print "the third computation took %3.8lf seconds" % dt

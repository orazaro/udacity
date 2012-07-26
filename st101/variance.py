#Complete the variance function to make it return the variance of a list of numbers
data3=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]
def mean(data):
    return sum(data)/len(data)
def variance(data):
    #Insert your code here
    mu = mean(data)
    s = 0
    for e in data:
        s += (e-mu)**2
    return s / len(data)

def variance_fast(data):
    mx, mx2, n = 0,0, len(data)
    for e in data:
        mx2 += e*e
        mx += e
    return mx2/n - (mx/n)**2 

print variance(data3)
print variance_fast(data3)

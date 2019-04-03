l1 = [1,2,3,4,5]
def x(x):
    return  x*x

print(list(map(x,l1)))
l1 = ['xiaoMing','zhAOsI']

def y(s1):
    s2=s1[0].upper()+s1[1:].lower()
    return s2

print(list(map(y,l1)))

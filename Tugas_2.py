from functools import reduce

def tri(x):
    return reduce(lambda x,y: x+y , range(1,x+1))

print(tri(3))
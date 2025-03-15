a=[1,2,3]
b=[3,4,5]
c=map(lambda x,y: x+y, a,b)
print(list(c))
d=[1,2,3,4,5]
def square(n):
    return n*n
e=list(map(square,d))
print(e)
    

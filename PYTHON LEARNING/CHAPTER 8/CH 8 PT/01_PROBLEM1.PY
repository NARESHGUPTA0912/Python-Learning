
def greatest(a, b ,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a = 111
b = 27
c = 3

print(greatest(a, b, c))
def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)

def f2(n,m):
    if n==1:
        return m
    else:
        return f2(n-1,n*m)

print(f2(10,2))
#print f2(999,1)
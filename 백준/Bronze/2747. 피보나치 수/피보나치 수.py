n = int(input())
d=[]
def fibo(n):
    d.append(0)
    d.append(1)
    for i in range(2, n+1):
        d.append(d[i-1] + d[i-2])
    return d[-1]    

print(fibo(n))
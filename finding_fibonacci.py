def fib(n=8):
    a, b = 0,1
    res = [0]
    for i in range(n-1):
        res.append(b)
        a,b=b,a+b
    return res
fib(10)
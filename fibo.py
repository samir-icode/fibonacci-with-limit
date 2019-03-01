n = int(input("Set fibonaci: "))
lnt = int(input("Set limit for number to generate: "))

def fibo(n):
    a,b =0,1
    res=[]
    while a<n:
        res.append(a)
#        print(a)

        a,b = b,a+b
#    print(res) print full list
    for lmt in res[0:lnt]:
        print(lmt)
          

fib = fibo(n)

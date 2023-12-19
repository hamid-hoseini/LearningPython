import timeit

def fib_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_2(n-1) + fib_2(n-2)
    
def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b,a+b
    return a   


t1 = timeit.Timer("fib(36)", "from greetings import fib")
print(t1.timeit(5))
# result: 7.670954801142216e-06

t2 = timeit.Timer("fib_2(36)", "from greetings import fib_2")
print(t2.timeit(5))
# result: 15.113292891066521

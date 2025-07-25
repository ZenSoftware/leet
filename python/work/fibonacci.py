def fib(n: int) -> int:
    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a+b
    return b

for n in range(10):
    print(fib(n))
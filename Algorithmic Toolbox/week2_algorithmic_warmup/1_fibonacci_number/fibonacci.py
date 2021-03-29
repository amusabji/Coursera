# Uses python3
def calc_fib(n):

    a = 0
    b = 1
    c = 1

    if n <= 1:
        return n
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return c

    # if (n <= 1):
    #     return n

    # return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(calc_fib(n))

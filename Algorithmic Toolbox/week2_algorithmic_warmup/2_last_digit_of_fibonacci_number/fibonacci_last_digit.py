# Uses python3
import sys
# import functools # only used during caching recursive calls

# def last_digit_of_fibonacci_number(n): # List from bottom up approach:
#     ## Error code during submission:
#     # Failed case #9/10: memory limit exceeded
#     # Input:
#     # 613455

#     # Your output:

#     # stderr:

#     # (Time used: 1.86/5.00, memory used: 2136485888/536870912.)
#     assert 0 <= n <= 10 ** 7

#     fib_list = [0, 1]
#     for i in range(2, n+1):
#         fib_list.append(fib_list[-1] + fib_list[-2])
#     return fib_list[n] % 10



# @functools.lru_cache(None)
# def last_digit_of_fibonacci_number(n):
#     ## Error Code during submission:
#     # Failed case #5/10: Cannot check answer. Perhaps output format is wrong.

#     # Input:
#     # 1000

#     # Your output:

#     # Your stderr:
#     # Traceback (most recent call last):
#     #   File "fibonacci_last_digit.py", line 24, in <module>
#     #     print(last_digit_of_fibonacci_number(n))
#     #   File "fibonacci_last_digit.py", line 19, in last_digit_of_fibonacci_number
#     #     return (last_digit_of_fibonacci_number(n-1) + last_digit_of_fibonacci_number(n-2)) % 10
#     #   File "fibonacci_last_digit.py", line 19, in last_digit_of_fibonacci_number
#     #     return (last_digit_of_fibonacci_number(n-1) + last_digit_of_fibonacci_number(n-2)) % 10
#     #   File "fibonacci_last_digit.py", line 19, in last_digit_of_fibonacci_number
#     #     return (last_digit_of_fibonacci_number(n-1) + last_digit_of_fibonacci_number(n-2)) % 10
#     #   [Previous line repeated 329 more times]
#     #   File "fibonacci_last_digit.py", line 17, in last_digit_of_fibonacci_number
#     #     if n < 2:
#     # RecursionError: maximum recursion depth exceeded in comparison

#     # Correct output:
#     # 5
#     #  (Time used: 0.01/5.00, memory used: 9117696/536870912.)
#     if n < 2:
#         return n
#     return (last_digit_of_fibonacci_number(n-1) + last_digit_of_fibonacci_number(n-2)) % 10


def last_digit_of_fibonacci_number(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec == '1':
            v1, v2, v3 = v1+v2, v1, v2
    return v2 % 10


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(last_digit_of_fibonacci_number(n))

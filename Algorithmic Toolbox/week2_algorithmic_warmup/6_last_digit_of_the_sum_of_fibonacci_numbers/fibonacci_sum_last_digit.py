# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    f0 = 0
    f1 = 1
    if n <= 1:
        return n
    else:
        rem = n % 60
        if rem == 0:
            return 0
        for i in range(2, rem + 3):
            f = (f0 + f1) % 60
            f0 = f1
            f1 = f

        solution = f1-1
        return solution % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(last_digit_of_the_sum_of_fibonacci_numbers(n))

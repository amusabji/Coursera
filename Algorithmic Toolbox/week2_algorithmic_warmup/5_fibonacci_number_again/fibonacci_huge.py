# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = (v2*v2) % m
        v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
        if rec == '1':
            v1, v2, v3 = (v1+v2) % m, v1, v2
    return v2


# if __name__ == '__main__':
#     input_n, input_m = map(int, input().split())
#     print(fibonacci_number_again(input_n, input_m))



if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fibonacci_number_again(n, m))

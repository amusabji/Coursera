# Uses python3
import sys

def gcd(a, b):
    # assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    small = min(a, b)
    big = max(a, b)
    remainder = 1
    while remainder != 0:
        remainder = big % small
        big = small
        small = remainder
    return big


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    return a * b // gcd(a, b)

if __name__ == '__main__':
    # inputt = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm(a, b))
    # input_n = str(input())
    # a, b = map(int, input_n.split())
    # print(lcm_naive(a, b))


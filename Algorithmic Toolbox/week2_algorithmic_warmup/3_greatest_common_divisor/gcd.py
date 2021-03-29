# Uses python3
import sys

def gcd_naive(a, b):
    small = min(a, b)
    big = max(a, b)
    remainder = 1
    while remainder != 0:
        remainder = big % small
        big = small
        small = remainder
    return big

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))

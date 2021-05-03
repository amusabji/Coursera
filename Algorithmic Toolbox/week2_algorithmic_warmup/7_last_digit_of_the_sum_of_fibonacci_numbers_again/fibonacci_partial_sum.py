# Uses python3
import sys

def fibonacci_partial_sum(n):
    f0 = 0
    f1 = 1
 
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    else:

        rem = n % 60

        if(rem == 0):
            return 0

        for i in range(2, rem + 3):
            f =(f0 + f1)% 60
            f0 = f1
            f1 = f
 
        s = f1-1
        return(s)


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    ans = fibonacci_partial_sum(to)-fibonacci_partial_sum(from_-1)
    print(ans % 10)
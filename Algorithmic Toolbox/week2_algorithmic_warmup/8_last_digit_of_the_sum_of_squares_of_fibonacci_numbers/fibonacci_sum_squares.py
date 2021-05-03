# Uses python3
from sys import stdin

# def fibonacci_sum_squares_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current * current

#     return sum % 10
def fibonacci_sum_squares(n):
    # array = [0] * (n+2)
    # array[1] = 1
    # for i in range(2, len(array)):
    #     array[i] = array[i-1] + array[i-2]

    # return (array[n+1] * array[n]) % 10
    # if n == 0:
    #     return 0
    # v1, v2, v3 = 1, 1, 0
    # for rec in bin(n)[3:]:
    #     calc = v2*v2 % m
    #     v1, v2, v3 = v1*v1+calc % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
    #     if rec == '1':
    #         v1, v2, v3 = (v1+v2) % m, v1, v2
    # return v2

   previous, current = 0, 1
   n = n % 60
   if (n == 0): 
       return 0
   elif (n == 1): 
       return 1
   else:
       for _ in range(2,n+1):
           previous, current= current, (previous + current)%60
       return current
       
if __name__ == '__main__':
    # n = int(input())
    n = int(stdin.read())
    print(fibonacci_sum_squares(n)*fibonacci_sum_squares(n+1)%10)

# if __name__ == '__main__':
#     # n = int(stdin.read())
#     n = int(input())
#     curr = fibonacci_sum_squares(n)
#     # print(f'curr: {curr}')
#     next = n+1
#     next = fibonacci_sum_squares(next)
#     # print(f'next: {next}')
#     print((next*curr))

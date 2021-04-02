# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
    i = len(a) // 2
    while a[i] != x: 
        if right-left == 0:
            return -1
        if x < a[i]:
            right = i
            i = (right-left) // 2 + left
            continue
        if x > a[i]:
            left = i
            i = (right-left) // 2 + left
            continue
    return i    


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n = data[0]
#     m = data[n + 1]
#     a = data[1 : n + 1]
#     for x in data[n + 2:]:
#         # replace with the call to binary_search when implemented
#         print(linear_search(a, x), end = ' ')
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
x = 17
binary_search(a, x)
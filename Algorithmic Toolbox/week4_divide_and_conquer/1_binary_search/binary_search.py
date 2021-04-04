# Uses python3
import sys

# def binary_search(a, x):
#     left, right = 0, len(a)
#     # write your code here

# def linear_search(a, x):
#     for i in range(len(a)):
#         if a[i] == x:
#             return i
#     return -1

# def binary_search(keys, query):
#     # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
#     # assert 1 <= len(keys) <= 3 * 10 ** 4
#     n = len(keys)
#     middle = n // 2
#     if query == keys[middle]:
#         return middle
#     # left search:
#     elif query < keys[middle]:
#         keys = keys[:middle]
#         return binary_search(keys, query)
#     # right search:
#     elif query > keys[middle]:
#         keys = keys[middle+1:]
#         return binary_search(keys, query)
#     else:
#         return -1

def binary_search(a, x):
    a.sort()
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


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))
    input_queries = list(map(int, input().split()))
    # input_keys = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # q = 4
    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
    # print(binary_search(input_keys, q))

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n = data[0]
#     m = data[n + 1]
#     a = data[1 : n + 1]
#     for x in data[n + 2:]:
#         # replace with the call to binary_search when implemented
#         print(binary_search(a, x), end = ' ')

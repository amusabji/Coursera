# Uses python3
import sys

# def get_number_of_inversions(a, b, left, right):
#     number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
#     ave = (left + right) // 2
#     number_of_inversions += get_number_of_inversions(a, b, left, ave)
#     number_of_inversions += get_number_of_inversions(a, b, ave, right)
#     #write your code here
#     return number_of_inversions

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     b = n * [0]
#     print(get_number_of_inversions(a, b, 0, len(a)))
def merge(b, c):
    result = []
    inversions = 0
    while b and c:
        if b[0] <= c[0]:
            result.append(b.pop(0))
        else:
            result.append(c.pop(0))
            inversions += len(b)

    result += b or c
    return result, inversions


def merge_sort(a):
    if len(a) == 1:
        return a, 0

    mid = len(a) // 2
    left, left_inv = merge_sort(a[:mid])
    right, right_inv = merge_sort(a[mid:])

    merged, merged_inv = merge(left, right)
    return merged, merged_inv + left_inv + right_inv


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(merge_sort(a)[1])
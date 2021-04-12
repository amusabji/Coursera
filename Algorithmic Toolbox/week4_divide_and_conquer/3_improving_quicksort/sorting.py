# Uses python3
import sys
from random import randint


def partition3(array, left, right):
    lt = left
    i = left
    gt = right
    pivot = array[left]

    while i <= gt:
        if array[i] < pivot:
            array[lt], array[i] = array[i], array[lt]
            lt += 1
            i += 1
        elif array[i] > pivot:
            array[i], array[gt] = array[gt], array[i]
            gt -= 1
        else:
            i += 1

    return lt, gt


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]

    lt, gt = partition3(array, left, right)
    randomized_quick_sort(array, left, lt - 1)
    randomized_quick_sort(array, gt + 1, right)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

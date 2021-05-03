# Uses python3
import sys
import numpy

def partitions3(W, n, items):
    count = 0 
    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if items[j-1]<=i:
                temp = value[i-items[j-1]][j-1] + items[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W: count += 1

    if count < 3: print('0')
    else: print('1')

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    total_weight = sum(A)
    if n<3: 
        print('0')
    elif total_weight%3 != 0: 
        print('0')
    else:
        partitions3(total_weight//3, n, A)


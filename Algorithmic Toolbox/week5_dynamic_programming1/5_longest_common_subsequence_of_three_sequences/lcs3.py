#Uses python3

import sys

def lcs3(a, b, c):
    m = len(a)
    n = len(b)
    o = len(c)
    L = [[[0 for i in range(o+1)] for j in range(n+1)]
         for k in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if (i == 0 or j == 0 or k == 0):
                    L[i][j][k] = 0
                     
                elif (a[i-1] == b[j-1] and
                      a[i-1] == c[k-1]):
                    L[i][j][k] = L[i-1][j-1][k-1] + 1
 
                else:
                    L[i][j][k] = max(max(L[i-1][j][k],
                    L[i][j-1][k]),
                                    L[i][j][k-1])

    return L[m][n][o]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n1 = data[0]
    data = data[1:]
    s1 = data[:n1]
    data = data[n1:]
    n2 = data[0]
    data = data[1:]
    s2 = data[:n2]
    data = data[n2:]
    n3 = data[0]
    data = data[1:]
    s3 = data[:n3]

    print(lcs3(s1, s2, s3))

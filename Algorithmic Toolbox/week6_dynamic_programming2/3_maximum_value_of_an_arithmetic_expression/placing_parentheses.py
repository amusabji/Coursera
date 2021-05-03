import math

def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b


def MinAndMax(M, m, i, j, operators):
    min_value = math.inf
    max_value = -math.inf
    for k in range(i, j):
        a = calc(M[i][k], M[k+1][j], operators[k])
        b = calc(M[i][k], m[k+1][j], operators[k])
        c = calc(m[i][k], M[k+1][j], operators[k])
        d = calc(m[i][k], m[k+1][j], operators[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value


def get_maximum_value(dataset):
    op = dataset[1:len(dataset):2]
    d = dataset[0:len(dataset)+1:2]
    n = len(d)
    #iniitializing matrices/tables
    m = [[0 for i in range(n)] for j in range(n)]  #minimized values
    M = [[0 for i in range(n)] for j in range(n)]  #maximized values
    for i in range(n):
        m[i][i] = int(d[i])   #so that the tables will look like
        M[i][i] = int(d[i])   #[[i, 0, 0...], [0, i, 0...], [0, 0, i,...]]
    for s in range(1,n):   #here's where I get confused
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(M, m, i, j, op)
    return M[0][n-1]


if __name__ == "__main__":
    expression = input()
    # operators, operands = [], []

    # for i in expression:
    #     if i in ['+', '-', '*']:
    #         operators.append(i)
    #     else:
    #         operands.append(int(i))

    print(get_maximum_value(expression))
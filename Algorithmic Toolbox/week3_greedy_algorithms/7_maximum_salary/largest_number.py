#Uses python3

import sys

def IsGraterOrEqual(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))

def largestnumber(lst):
    answer = []
    
    while lst!=[]:
        max_digit = 0
        for digit in lst:
            if IsGraterOrEqual(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        lst.remove(max_digit)

    return answer



if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    lst = data[1:]
    # print(largest_number(a))
    print(''.join([str(i) for i in largestnumber(lst)]))

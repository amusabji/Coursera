#python3
import sys
# import time

def max_pairwise_product(numbers):
    # start_time = time.process_time()
    n = len(numbers)
    first = 0
    second = 0
    for i in range(n):
        if numbers[i] > second:
            if numbers[i] >= first:
                second = first
                first = numbers[i]
                continue
            second = numbers[i]
    # print(first * second)
    # print(time.process_time() - start_time)
    return first * second

# #my implementation of main:
# if __name__ == '__main__':
#     input_type = sys.argv[1]
#     if input_type == '-f':
#         with open('C:\\Users\\Me\\OneDrive\\Documents\\code\\Coursera\\'
#                     'Algorithmic Toolbox\\week1_programming_challenges\\'
#                     '2_maximum_pairwise_product\\input.txt') as inFile:
#             input_file = inFile.read()
#         input_numbers = [int(x) for x in input_file.split()]
#         max_pairwise_product(input_numbers)
#     elif input_type == '-i':
#         input_numbers = [int(x) for x in input().split()]
#         max_pairwise_product(input_numbers)

#original:
if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
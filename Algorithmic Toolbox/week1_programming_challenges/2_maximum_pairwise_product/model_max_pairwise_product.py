# python3
import sys
import time

def max_pairwise_product(numbers):
    start_time = time.process_time()
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])
    print(max_product)
    print(time.process_time() - start_time)
    return max_product

if __name__ == '__main__':
    # input_n = int(input())
    input_type = sys.argv[1]
    if input_type == '-f':
        with open('C:\\Users\\Me\\OneDrive\\Documents\\code\\Coursera\\'
                    'Algorithmic Toolbox\\week1_programming_challenges\\'
                    '2_maximum_pairwise_product\\input.txt') as inFile:
            input_file = inFile.read()
        # print(input_file.split())
        input_numbers = [int(x) for x in input_file.split()]
        max_pairwise_product(input_numbers)
        # with open('C:\\Users\\Me\\OneDrive\\Documents\\code\\Coursera\\'
        #             'Algorithmic Toolbox\\week1_programming_challenges\\'
        #             '2_maximum_pairwise_product\\model.txt', 'w') as outFile:
        #     output_file = outFile.write(str(max_pairwise_product(input_numbers)))
    elif input_type == '-i':
        input_numbers = [int(x) for x in input().split()]
        max_pairwise_product(input_numbers)
        # with open('C:\\Users\\Me\\OneDrive\\Documents\\code\\Coursera\\'
        #             'Algorithmic Toolbox\\week1_programming_challenges\\'
        #             '2_maximum_pairwise_product\\model.txt', 'r+') as outFile:
        #     output = str(max_pairwise_product(input_numbers))
        #     print("your output is:", output)
        #     outFile.write(output)
            # outFile.read()
    # print(max_pairwise_product(input_numbers))

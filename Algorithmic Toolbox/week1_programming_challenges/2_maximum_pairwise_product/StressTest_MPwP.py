import sys
import time
import random

def model_max_pairwise_product(numbers):
    # start_time = time.process_time()
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])
    # print(max_product)
    # print(time.process_time() - start_time)
    return max_product

def main_max_pairwise_product(numbers):
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



def main():
    while(True):
        print("I am working!")
        n = random.randint(1,50) 
        a = ' '.join([str(random.randint(1,1000)) for i in range(n)])
        a = [int(x) for x in a.split()]
        print("List Size:",len(a),"\n",a)
        res1 = main_max_pairwise_product(a)
        res2 = model_max_pairwise_product(a)
        if res1 != res2:
            print("Wrong Answer! res1:", res1, "res2:", res2)
            break
        else:
            print("Good")
main()
# n = int(sys.argv[1])
# with open('C:\\Users\\Me\\OneDrive\\Documents\\code\\Coursera\\'
# 'Algorithmic Toolbox\\week1_programming_challenges\\'
# '2_maximum_pairwise_product\\input.txt', 'w') as outFile:
#     output_file = outFile.write(' '.join([str(i*2) for i in range(n)]))
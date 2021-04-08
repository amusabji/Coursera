def binary_search(nums, target):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    # assert 1 <= len(keys) <= 3 * 10 ** 4
    # nums.sort()
    start = 0
    end = len(nums)

    if (target > nums[-1]) or (target < nums[0]):
        return -1

    while start <= end:
        mid = ((end + start)//2)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]
    input_keys.sort()
    for q in input_queries:
        print(binary_search(input_keys, q), end=" ")
# a = [-1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4]
# x = 0

# # Stress Test:
# n = random.randint(1,3*10**4) 
# a = list((random.randint(1,10)) for i in range(n))
# input_queries = list((random.randint(-1,15)) for i in range(n))
# for k in range(1):
#     n = random.randint(1,3*10**4) 
#     a = list((random.randint(1,1000)) for i in range(n))
#     input_queries = list((random.randint(-10,1500)) for i in range(n))
#     start_time = time.process_time()
#     print(f'a: {a}, input_queries: {input_queries}, n: {n}')
#     for q in input_queries:
#         print(binary_search(a, q), end=" ")
#     print(f'execution time: {time.process_time() - start_time}')
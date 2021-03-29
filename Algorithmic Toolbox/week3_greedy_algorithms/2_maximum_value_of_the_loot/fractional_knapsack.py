# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    # value variable
    current_value_in_knapsack = 0
    # create and add to value_dict
    n = len(weights)
    value_dict = {}
    for i in range(n):
        value_dict.update({i: values[i]/weights[i]})

    # create sorted list of values
    values_list = list(value_dict.values())
    values_list.sort(reverse=True)

    # start adding highest valued items to bag while there's room
    while (capacity != 0 and values_list):
        # find index of highest valued item
        ind = list(value_dict.keys())[list(value_dict.values()).index(values_list[0])]
        # calculate and add value to total value
        current_weight_of_item = min(capacity, weights[ind])
        current_value_in_knapsack = current_value_in_knapsack + (current_weight_of_item * value_dict.get(ind))
        # remove capacity
        capacity = capacity - current_weight_of_item
        # update values list so highest valued item is no longer in list
        values_list.remove(values_list[0])
    return current_value_in_knapsack


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    # data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

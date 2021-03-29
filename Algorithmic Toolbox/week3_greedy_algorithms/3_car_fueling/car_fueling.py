# python3
import sys


def compute_min_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 <= stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] <= d

    num_refills = 0
    current_refill = 0
    stops.insert(0, 0)
    stops.append(d)
    n = len(stops) - 2
    while current_refill <= n:
        last_refill = current_refill
        while current_refill <= n and (stops[current_refill + 1]-stops[last_refill] <= m):
            current_refill += 1
        if current_refill == last_refill:
            return -1
        if current_refill <= n:
            num_refills += 1
    return num_refills

# if __name__ == '__main__':
#     d, m, *stops = map(int, input().split())
#     print(compute_min_refills(d, m, stops))
if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
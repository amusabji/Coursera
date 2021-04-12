# python3

from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared(points):
    x_sorted = sorted(points, key=lambda x: x[0])
    y_sorted = sorted(points, key=lambda x: x[1])
    p1, p2, mi = closest_pair(x_sorted, y_sorted)
    return mi


def closest_pair(sorted_x, sorted_y):
    if len(sorted_x) <= 3:
        return brute(sorted_x)
    mid = len(sorted_x) // 2
    q_x = sorted_x[:mid]
    r_x = sorted_x[mid:]

    midpoint = sorted_x[mid][0]
    q_y = list()
    r_y = list()
    for i in sorted_y:
        if i[0] <= midpoint:
            q_y.append(i)
        else:
            r_y.append(i)

    (p1, q1, mi1) = closest_pair(q_x, q_y)
    (p2, q2, mi2) = closest_pair(r_x, r_y)
    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)

    (p3, q3, mi3) = closest_split_pair(sorted_x, sorted_y, d, mn)

    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3


def closest_split_pair(p_x, p_y, delta, best_pair):
    mx_x = p_x[len(p_x) // 2][0]
    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
    best = delta
    for i in range(len(s_y) - 1):
        for j in range(i+1, min(i + 7, len(s_y))):
            p, q = s_y[i], s_y[j]
            dst = distance_squared(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best


def brute(sorted_x):
    mi = distance_squared(sorted_x[0], sorted_x[1])
    p1 = sorted_x[0]
    p2 = sorted_x[1]
    if len(sorted_x) == 2:
        return p1, p2, mi
    for i in range(len(sorted_x)-1):
        for j in range(i + 1, len(sorted_x)):
            if i != 0 and j != 1:
                d = distance_squared(sorted_x[i], sorted_x[j])
                if d < mi:  # Update min_dist and points
                    mi = d
                    p1, p2 = sorted_x[i], sorted_x[j]
    return p1, p2, mi


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
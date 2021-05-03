# Uses python3
import sys


def optimal_sequence(n):
    hops = [0] * (n + 1)
    hops[1] = 1
    for i in range(2, n + 1):
        idx = [i - 1]
        if i % 2 == 0:
            idx.append(i // 2)
        if i % 3 == 0:
            idx.append(i // 3)

        min_hops = min([hops[x] for x in idx])

        hops[i] = min_hops + 1

    current = n
    optimal = [current]
    while current != 1:

        possible = [current - 1]
        if current % 2 == 0:
            possible.append(current // 2)
        if current % 3 == 0:
            possible.append(current // 3)
        current = min(
            [(p, hops[p]) for p in possible],
            key=lambda x: x[1]
        )[0]
        optimal.append(current)

    return reversed(optimal)


input = sys.stdin.read()  # uncomment this when submitting
n = int(input)  # remove the '()' from input() when submitting
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

# Uses python3
import sys


def get_change(money):
    coins = [1, 3, 4]
    dp = [money + 1] * (money + 1)
    dp[0] = 0

    for i in range(1, money + 1):
        for j in range(0, len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    return -1 if dp[money] > money else dp[money]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = int(input())
    print(get_change(m))

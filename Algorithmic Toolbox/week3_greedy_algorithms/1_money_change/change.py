# Uses python3
import sys

def get_change(m):
    #write your code here
    dimes = m // 10
    change = m % 10
    if change >= 5:
        nickle = 1
        pennies = change - 5
        return dimes + nickle + pennies
    return dimes + change
    # return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

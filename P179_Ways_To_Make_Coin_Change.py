# prob_link: https://www.codingninjas.com/studio/problems/ways-to-make-coin-change_8230691?challengeSlug=striver-sde-challenge&leftPanelTab=0

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)


def countWaysToMakeChange(denominations, value):
    # Your code goes here
    def count(coins, n, sum):
        if (sum == 0):
            return 1
        if (sum, n) in mp:
            return mp[(sum, n)]
        if (sum < 0):
            return 0

        if (n <= 0):
            return 0
        x = count(coins, n - 1, sum)
        y = count(coins, n, sum - coins[n - 1])
        mp[(sum, n)] = x + y
        return mp[(sum, n)]

    mp = {}
    return count(denominations, len(denominations), value)


# taking inpit using fast I/O
def takeInput():
    numDenominations = int(input())

    denominations = list(map(int, stdin.readline().strip().split(" ")))

    value = int(input())
    return denominations, numDenominations, value


# main
denominations, numDenomination, value = takeInput()
print((countWaysToMakeChange(denominations, value)))
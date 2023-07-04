# prob_link: https://www.codingninjas.com/studio/problems/rod-cutting-problem_8230727?challengeSlug=striver-sde-challenge&leftPanelTab=0

from sys import stdin
import sys

def cutRod(prices, n):

    # Write your code here.
    mat = [[0 for i in range(n+1)]for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1:
                mat[i][j] = j*prices[i-1]
            else:
                if i > j:
                    mat[i][j] = mat[i-1][j]
                else:
                    mat[i][j] = max(prices[i-1]+mat[i][j-i], mat[i-1][j])
    return mat[n][n]

# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


# Main.
t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1

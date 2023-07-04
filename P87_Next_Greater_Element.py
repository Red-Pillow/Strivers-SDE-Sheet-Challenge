# prob_link: https://www.codingninjas.com/studio/problems/next-greater-element_8230718?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin


def nextGreater(arr, n):
    # Your code goes here

    s = []
    for i in range(len(arr)):
        while s and s[-1].get("value") < arr[i]:
            d = s.pop()
            arr[d.get("ind")] = arr[i]
        s.append({"value": arr[i], "ind": i})
    while s:
        d = s.pop()
        arr[d.get("ind")] = -1
    return arr


# Main

t = int(stdin.readline().rstrip())

while t > 0:

    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    z = (nextGreater(arr, n))
    for i in z:
        print(i, end=" ")
    print()

    t -= 1

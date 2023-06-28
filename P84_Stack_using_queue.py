# prob_link: https://www.codingninjas.com/studio/problems/stack-using-queue_8230715?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)


class Stack:
    def __init__(self):
        # Intitialize your data structure here.
        self.dq = deque()

    def getSize(self):
        # Implement the getSize() function.
        return len(self.dq)

    def isEmpty(self):
        return self.getSize() == 0

    def push(self, ele):
        # Implement the push() function.
        self.dq.append(ele)

    def pop(self):
        if len(self.dq) == 0:
            return -1
        return self.dq.pop()

    def top(self):
        if self.getSize() == 0:
            return -1
        return self.dq[-1]


def takeInput():
    values = list(map(int, stdin.readline().strip().split(" ")))
    return values


#  main
st = Stack()
q = int(stdin.readline().strip())

stack = Stack()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2:
        print(stack.pop())

    elif choice == 3:
        print(stack.top())

    elif choice == 4:
        print(stack.getSize())

    else:
        if stack.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1
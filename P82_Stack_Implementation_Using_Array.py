# Prob_link: https://www.codingninjas.com/codestudio/problems/stack-implementation-using-array_8230854?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *


# Stack class.
class Stack:

    def __init__(self, capacity: int):
        # Write your code here.
        self.cap = capacity
        self.stack = []

    def push(self, num: int) -> None:
        # Write your code here.
        if len(self.stack) < self.cap:
            self.stack.append(num)

    def pop(self) -> int:
        # Write your code here.
        if self.stack:
            return self.stack.pop()
        return -1

    def top(self) -> int:
        # Write your code here.
        if self.stack:
            return self.stack[-1]
        return -1

    def isEmpty(self) -> int:
        # Write your code here.
        if len(self.stack) == 0:
            return 1
        return 0

    def isFull(self) -> int:
        # Write your code here.
        if len(self.stack) == self.cap:
            return 1
        return 0


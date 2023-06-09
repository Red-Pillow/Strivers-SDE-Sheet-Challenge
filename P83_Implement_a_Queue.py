# Prob_link: https://www.codingninjas.com/codestudio/problems/implement-a-queue_8230848?challengeSlug=striver-sde-challenge&leftPanelTab=1
from os import *
from sys import *
from collections import *
from math import *


class Queue:

    # Define data members and __init__()
    def __init__(self):
        self.queue = []
        self.var = 0

    '''----------------- Public Functions of Queue -----------------'''

    def isEmpty(self):
        # Implement the isEmpty() function
        return len(self.queue) == 0

    def enqueue(self, x):
        # Implement the enqueue(element) function
        self.queue.append(x)

    def dequeue(self):
        # Implement the dequeue() function
        if not self.queue:
            return -1
        return self.queue.pop(0)

    def front(self):
        if not self.queue:
            return -1
        # Implement the front() function
        return self.queue[0]
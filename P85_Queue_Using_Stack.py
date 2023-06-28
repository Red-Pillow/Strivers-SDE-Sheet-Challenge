# prob_link: https://www.codingninjas.com/studio/problems/day-25-queue-using-stack_8230722?challengeSlug=striver-sde-challenge&leftPanelTab=0

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)
from collections import deque
class Queue:

    def __init__(self):
        # Initialize your data structure here.
        self.dq = deque()

    def enQueue(self, val):
        # Implement the enqueue() function.
        self.dq.append(val)

    def deQueue(self):
        # Implement the dequeue() function.
        if len(self.dq)==0:
            return -1
        return self.dq.popleft()

    def peek(self):
        # Implement the peek() function here.
        if len(self.dq)==0:
            return -1
        return self.dq[0]

    def isEmpty(self):
        # Implement the isEmpty() function here.
        return len(self.dq)==0

# Taking input.
def takeInput():
    n = int(input())

    obstacles = list(map(int, input().strip().split(" ")))

    return obstacles, n

# Main.
q = Queue()
queries = int(input())
while queries:
    values = []
    values = input().split(" ")
    values[0] = int(values[0])
    if values[0] == 1:
        values[1] = int(values[1])
        q.enQueue(values[1])
    elif values[0] == 2:
        print(q.deQueue())
    elif values[0] == 3:
        print(q.peek())
    elif values[0] == 4:
        print(str(q.isEmpty()).lower())
    queries = queries - 1

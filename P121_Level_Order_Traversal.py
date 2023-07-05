# prob_link: https://www.codingninjas.com/studio/problems/level-order-traversal_8230716?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)


#   Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def getLevelOrder(root):
    if not root:
        return []
    #   Write your code here
    from collections import deque
    dq = deque()
    if not root:
        return 0
    dq.append(root)
    maxi = 0
    ans = []
    while(dq):
        size = len(dq)
        level = []
        maxi = max(maxi,len(dq))
        for i in range(size):
            popped = dq.popleft()
            level.append(popped.val)
            if popped.left:
                dq.append(popped.left)
            if popped.right:
                dq.append(popped.right)
        ans.extend(level)
    return ans







































#   Fast input
def takeInput():

    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1):
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()

        leftChild = arr[index]

        if(leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if(rightChild != -1):
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)

        index += 1

    return root


def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()


# main
T = int(stdin.readline().strip())
for i in range(T):
    root = takeInput()
    ans = getLevelOrder(root)
    printAns(ans)

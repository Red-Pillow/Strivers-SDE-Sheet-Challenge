# prob_link: https://www.codingninjas.com/studio/problems/top-view-of-binary-tree_8230721?challengeSlug=striver-sde-challenge&leftPanelTab=0


from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
from queue import Queue

setrecursionlimit(10 ** 7)


# Following is the TreeNode class structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def getTopView(root):
    # Write your code here.

    def topView(head, dis, level, dict):

        if head is None:
            return

        if dis not in dict or level < dict[dis][1]:
            dict[dis] = (head.val, level)
        topView(head.left, dis - 1, level + 1, dict)
        topView(head.right, dis + 1, level + 1, dict)

    def printTopView(head):
        dict = {}

        topView(root, 0, 0, dict)
        ans = []
        for key in sorted(dict.keys()):
            ans.append(dict.get(key)[0])
        return ans

    return printTopView(root)


# Taking input.
def takeInput():
    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if (rootData == -1):
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while (q.qsize() > 0):
        currentNode = q.get()

        leftChild = arr[index]

        if (leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if (rightChild != -1):
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

        index += 1

    return root


# Printing the tree nodes.
def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()


# Main.
T = int(stdin.readline().strip())
for i in range(T):
    root = takeInput()
    ans = getTopView(root)
    printAns(ans)
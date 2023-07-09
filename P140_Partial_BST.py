# Prob_link: https://www.codingninjas.com/studio/problems/partial-bst_8230723?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

import queue
import sys

sys.setrecursionlimit(10 ** 6)


class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root, arr):
    if root:
        inorder(root.left, arr)

        arr.append(root.data)

        inorder(root.right, arr)


def validateBST(root):
    arr = []

    inorder(root, arr)

    for i in range(1, len(arr)):

        if arr[i - 1] > arr[i]:
            return False

    return True


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)

    if length <= 0 or levelorder[0] == -1:
        return None

    root = BinaryTreeNode(levelorder[index])
    index += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():

        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelorder[index]
        index += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


t = int(sys.stdin.readline().strip())
while t > 0:

    li = list(map(int, sys.stdin.readline().strip().split(" ")))
    root = buildLevelTree(li)
    if (validateBST(root)):
        print('true')
    else:
        print('false')
    t = t - 1




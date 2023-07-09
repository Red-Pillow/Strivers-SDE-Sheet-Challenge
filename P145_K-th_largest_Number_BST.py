# Prob_link: https://www.codingninjas.com/studio/problems/k-th-largest-number-bst_8230750?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

'''

    ------- Binary Tree node structure --------
            class TreeNode :
                def __init__(self, data):
                    self.data = data
                    self.left = None
                    self.right = None

                def __del__(self):
                    if self.left:
                        del self.left
                    if self.right:
                        del self.right

'''
import heapq


def KthLargestNumber(root, k):
    arr = []

    q = [root]

    while q:

        node = q.pop(0)

        val = node.data

        if len(arr) < k:

            heapq.heappush(arr, val)

        else:

            heapq.heappush(arr, val)

            heapq.heapify(arr)

            heapq.heappop(arr)

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)

    if len(arr) < k:
        return -1

    return arr[0]
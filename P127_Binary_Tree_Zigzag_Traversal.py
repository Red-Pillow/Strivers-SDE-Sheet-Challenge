# prob_link: https://www.codingninjas.com/studio/problems/binary-tree-zigzag-traversal_8230796?challengeSlug=striver-sde-challenge&leftPanelTab=0
from os import *
from sys import *
from collections import *
from math import *


# BinaryTreeNode class definition
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#

def zigZagTraversal(root):
    # Write your code here
    if not root:
        return []
    from collections import deque

    dq = deque()
    dq.append(root)
    ans = []
    c = 0
    while (len(dq)):
        temp = []
        for i in range(len(dq)):
            x = dq.popleft()
            temp.append(x.data)
            if x.left:
                dq.append(x.left)
            if x.right:
                dq.append(x.right)

        if c % 2 != 0:
            temp = temp[::-1]
            ans.extend(temp)
        else:
            ans.extend(temp)
        c += 1
    return ans

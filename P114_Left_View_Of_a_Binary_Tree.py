# prob_link: https://www.codingninjas.com/studio/problems/left-view-of-a-binary-tree_8230757?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *


# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getLeftView(root) -> list:
    # Write your code here
    # Return a list
    if not root:
        return []
    from collections import deque
    dq = deque()
    ans = []
    dq.append(root)
    while (len(dq) > 0):
        level = []
        size = len(dq)
        while (size > 0):
            popped = dq.popleft()
            level.append(popped.data)
            if popped.left:
                dq.append(popped.left)
            if popped.right:
                dq.append(popped.right)
            size -= 1
        if len(level) > 0:
            ans.append(level[0])

    return ans
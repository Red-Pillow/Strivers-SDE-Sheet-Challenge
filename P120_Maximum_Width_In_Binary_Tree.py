# prob_link: https://www.codingninjas.com/studio/problems/maximum-width-in-binary-tree_8230710?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

def getMaxWidth(root):
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
        ans.append(level)
    return maxi
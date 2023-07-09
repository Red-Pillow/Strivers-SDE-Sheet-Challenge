# Prob_link: https://www.codingninjas.com/studio/problems/bst-iterator_8230815?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

'''
Binary tree node class for reference

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''


class BSTiterator:
    def __init__(self, root):
        self.st = []
        while root:
            self.st.append(root)
            root = root.left

    def next(self):
        res = self.st.pop()
        curr = res.right
        while curr:
            self.st.append(curr)
            curr = curr.left
        return res.data

    def hasNext(self):
        return self.st != []


'''
    Your BSTIterator object will be instantiated and called as such:
    BSTIterator iterator(root)
    while(iterator.hasNext()):
       print(iterator.next())
'''


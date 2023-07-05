# prob_link: https://www.codingninjas.com/studio/problems/lca-of-two-nodes-in-a-bst_8230778?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

# Binary Tree node structure
class   TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right


def LCAinaBST(root, p, q):

    # Write your code here
    # P and Q are the given nodes
    # Return LCA node
    cur = root
    while(cur):
        if cur.data>p.data and cur.data>q.data:
            cur = cur.left
        elif cur.data<p.data and cur.data<q.data:
            cur = cur.right
        else:
            return cur
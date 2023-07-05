# prob_link: https://www.codingninjas.com/studio/problems/check-identical-trees_8230719?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *


# Following is the Binary Tree Node class structure
class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def identicalTrees(p, q):
    # Your code goes here.
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.data != q.data:
        return False
    return identicalTrees(p.left, q.left) and identicalTrees(p.right, q.right)

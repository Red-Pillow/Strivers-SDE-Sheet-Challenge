# prob_link: https://www.codingninjas.com/studio/problems/search-in-bst_8230841?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the Binary Tree node structure:

	class BinaryTreeNode :
	    def __init__(self, data) :
	        self.data = data
	        self.left = None
	        self.right = None

'''

def searchInBST(root, x):
	# Write your code here.
    curr=root
    while curr:
        if curr.data==x:
            return True
        elif curr.data>x:
            curr=curr.left
        else:
            curr=curr.right
    return False
# Prob_link: https://www.codingninjas.com/studio/problems/connect-nodes-at-same-level_8230790?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *

from sys import *

from collections import *

from math import *

'''

    ----------------- Binary Tree node class for reference -----------------



    class BinaryTreeNode:

        def __init__(self, data):

            self.data = data

            self.left = None

            self.right = None

            self.next = None

'''


def connectNodes(root):
    # edge case check

    if not root:
        return None

    # initialize the queue with root node (for level order traversal)

    queue = deque([root])

    # start the traversal

    while queue:

        size = len(queue)  # get number of nodes on the current level

        for i in range(size):

            node = queue.popleft()  # pop the node

            # An important check so that we do not wire the node to the node on the next level.

            if i < size - 1:
                node.next = queue[0]  # because the right node of the popped node would be the next in the queue.

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return root
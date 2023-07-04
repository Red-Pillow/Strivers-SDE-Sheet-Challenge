# prob_link: https://www.codingninjas.com/studio/problems/bottom-view-of-binary-tree_8230745?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
import queue
import sys
from collections import OrderedDict

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bottomView(root):
    # Write your code here.
    # This function returns a list of nodes which is the required bottom view of the tree.
    if (root == None):
        return

    # Initialize a variable 'hd' with 0
    # for the root element.
    hd = 0

    # Store minimum and maximum horizontal distance
    # so that we do not have to sort keys at the end
    min_hd, max_hd = 0, 0

    hd_dict = dict()

    # Queue to store tree nodes in level
    # order traversal
    q = deque()

    # Assign initialized horizontal distance
    # value to root node and add it to the queue.
    root.hd = hd
    q.append(root)

    # Loop until the queue is empty (standard
    # level order loop)
    while q:
        curr_node = q.popleft()

        # Extract the horizontal distance value
        # from the dequeued tree node.
        hd = curr_node.hd

        # Update the minimum and maximum hd
        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        # Put the dequeued tree node to dictionary
        # having key as horizontal distance. Every
        # time we find a node having same horizontal
        # distance we need to update the value in
        # the map.
        hd_dict[hd] = curr_node.data

        # If the dequeued node has a left child, add
        # it to the queue with a horizontal distance hd-1.
        if curr_node.left:
            curr_node.left.hd = hd - 1
            q.append(curr_node.left)

        # If the dequeued node has a right child, add
        # it to the queue with a horizontal distance
        # hd+1.
        if curr_node.right:
            curr_node.right.hd = hd + 1
            q.append(curr_node.right)

    # Traverse the map from least horizontal distance to
    # most horizontal distance.
    ans = []
    for i in range(min_hd, max_hd + 1):
        ans.append(hd_dict[i])
    return ans


# Taking level-order input using fast I/O method.
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


# Main.
t = int(input())
while t:
    root = takeInput()
    answer = bottomView(root)
    print(*answer)
    t = t - 1

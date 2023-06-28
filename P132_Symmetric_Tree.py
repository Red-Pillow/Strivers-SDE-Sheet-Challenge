# prob_link: https://www.codingninjas.com/studio/problems/symmetric-tree_8230686?challengeSlug=striver-sde-challenge&leftPanelTab=0

'''

    Following is the representation for the Binary Tree Node:

    class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
'''


def isSymmetric(root):
    # Write your code here.
    if not root:
        return True

    def check(p, q):

        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.data != q.data:
            return False
        return check(p.left, q.right) and check(p.right, q.left)

    return check(root.left, root.right)

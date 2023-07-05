# prob_link: https://www.codingninjas.com/studio/problems/diameter-of-binary-tree_8230762?challengeSlug=striver-sde-challenge&leftPanelTab=0


# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameterOfBinaryTree(root):
    # Write your code here
    # Return the root of the tree
    def traverse(root):
        if root is None:
            return 0
        l = traverse(root.left)
        r = traverse(root.right)
        maxi[0] = max(maxi[0], l + r)
        return 1 + max(l, r)

    maxi = [0]
    traverse(root)
    return maxi[0]
# Prob_link: https://www.codingninjas.com/studio/problems/tree-traversals_8230775?challengeSlug=striver-sde-challenge&leftPanelTab=0

def getTreeTraversal(root):
    # Write your code here.
    st = []
    st.append([root, 1])  # stack :pair(root value,index)
    pre = []
    inor = []
    post = []
    if root is None:
        return []
    while len(st) > 0:
        it = st[-1]
        # when the index value is 1 value is added to preorder and the value of index is incremented
        if it[1] == 1:
            st[-1][1] += 1
            pre.append(it[0].data)

            if it[0].left:
                st.append([it[0].left, 1])
        # the incremented index is then used for inorder
        elif (it[1] == 2):
            st[-1][1] += 1
            inor.append(it[0].data)
            if it[0].right:
                st.append([it[0].right, 1])
        else:
            post.append(it[0].data)
            del st[-1]

    return [inor, pre, post]
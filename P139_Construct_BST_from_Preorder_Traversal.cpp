# Prob_link: https://www.codingninjas.com/studio/problems/construct-bst-from-preorder-traversal_8230850?challengeSlug=striver-sde-challenge&leftPanelTab=0


#include <bits/stdc++.h>

TreeNode<int> *constructTree(vector<int> &arr, int low, int high) {
  if (low > high)
    return NULL;

  int mid = (low + high) / 2;
  TreeNode<int> *root = new TreeNode<int>(arr[mid]);

  root->left = constructTree(arr, low, mid - 1);
  root->right = constructTree(arr, mid + 1, high);

  return root;
}

TreeNode<int> *preOrderTree(vector<int> &preOrder) {
  sort(preOrder.begin(), preOrder.end());
  return constructTree(preOrder, 0, preOrder.size() - 1);
}
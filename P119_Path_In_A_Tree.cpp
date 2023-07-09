# Prob_link: https://www.codingninjas.com/studio/problems/path-in-a-tree_8230860?challengeSlug=striver-sde-challenge&leftPanelTab=0

#include <bits/stdc++.h>
/*
    template <typename T = int>
	class TreeNode
	{
		public:
		T data;
		TreeNode<T> *left;
		TreeNode<T> *right;

		TreeNode(T data)
		{
			this->data = data;
			left = NULL;
			right = NULL;
		}

		~TreeNode()
		{
			if (left != NULL)
			{
		  		delete left;
			}
			if (right != NULL)
			{
			 	delete right;
			}
		}
	};
*/


bool chk(TreeNode<int>*node,int x, vector<int>&v)
{
	if(!node) return false;
	v.push_back(node->data);
	if(chk(node->left,x,v) or chk(node->right,x,v))
	return true;
	if(node->data ==x) return true;
	v.pop_back();
	return false;
}

vector<int> pathInATree(TreeNode<int> *root, int x)
{
	vector<int> v;
    if(!root) return {};
	chk(root,x,v);
	return v;
}
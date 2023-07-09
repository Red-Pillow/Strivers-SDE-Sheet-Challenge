# Prob_link: https://www.codingninjas.com/studio/problems/convert-a-given-binary-tree-to-doubly-linked-list_8230744?challengeSlug=striver-sde-challenge&leftPanelTab=0



#include <bits/stdc++.h>

BinaryTreeNode<int>* BTtoDLL(BinaryTreeNode<int>* root) {

 BinaryTreeNode<int>*head=NULL,*prev=NULL,*cur=root;

    while(cur){

        if(cur->left==NULL){

            if(head==NULL)//whenever reached the leftmost end that is the head of the dll

                head=cur;

            cur->left=prev;

            if(prev!=NULL)

                prev->right=cur;

            prev=cur;

            cur=cur->right;

        }

        else{

            BinaryTreeNode<int>*pred=cur->left;

            while(pred->right!=NULL && pred->right!=cur)

                pred=pred->right;

            if(pred->right==NULL){

                pred->right=cur;

                cur=cur->left;

            }

            else{

                cur->left=prev;//since the right side link is already present

                prev=cur;

                cur=cur->right;

            }

        }

    }

    return head;

}
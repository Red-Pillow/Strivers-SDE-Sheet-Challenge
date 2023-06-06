# Prob_link: https://www.codingninjas.com/codestudio/problems/palindrome-linked-list_8230717?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin


# Following is the class structure of the LinkedListNode class:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def isPalindrome(head):
    temp = head
    p = []
    while (temp):
        p.append(temp.data)
        temp = temp.next
    # Write your code here.
    return p == p[::-1]


def takeinput():
    inputlist = [int(ele) for ele in input().split()]

    head = None
    tail = None

    for currentData in inputlist:

        if currentData == -1:
            break

        Newnode = Node(currentData)

        if head is None:
            head = Newnode
            tail = Newnode
        else:
            tail.next = Newnode
            tail = Newnode

    return head


# Main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeinput()

    if isPalindrome(head):
        print('true')
    else:
        print('false')

    t -= 1


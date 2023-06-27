# prob_link: https://www.codingninjas.com/studio/problems/merge-two-sorted-linked-lists_8230729?challengeSlug=striver-sde-challenge&leftPanelTab=0

from math import *
from collections import *
from sys import *
from os import *

import sys
from sys import stdin


# Following is the linked list node structure:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sortTwoLists(l1, l2):
    # Write your code here.

    if l1 == None:
        return l2
    if not l2:
        return l1
    dummy = Node(23)
    head = dummy
    while (l1 and l2):
        if l1.data <= l2.data:
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next
        dummy = dummy.next
    if l1:
        dummy.next = l1
    if l2:
        dummy.next = l2
    return head.next


def ll(arr):
    if len(arr) == 0:
        return None

    head = Node(arr[0])
    last = head

    for data in arr[1:]:
        last.next = Node(data)
        last = last.next

    return head


def printll(head):
    while head:
        print(head.data, end=' ')

        head = head.next

    print(-1)


t = int(sys.stdin.readline().strip())

for i in range(t):
    arr1 = list(map(int, sys.stdin.readline().strip().split(" ")))
    arr2 = list(map(int, sys.stdin.readline().strip().split(" ")))

    l1 = ll(arr1[:-1])
    l2 = ll(arr2[:-1])

    l = sortTwoLists(l1, l2)

    printll(l)


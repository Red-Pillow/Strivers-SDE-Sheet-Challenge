# prob_link: https://www.codingninjas.com/codestudio/problems/copy-list-with-random-pointer_8230734?challengeSlug=striver-sde-challenge&leftPanelTab=0

from math import *
from collections import *
from sys import *
from os import *


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


def cloneRandomList(head):
    # Your code goes here.
    cur = head
    dicti = {}
    while cur:
        dicti[cur] = LinkedListNode(cur.data)
        cur = cur.next
    dicti[None] = None
    cur = head
    while cur:
        dicti[cur].next = dicti[cur.next]
        dicti[cur].random = dicti[cur.random]
        cur = cur.next
    return dicti[head]

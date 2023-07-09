# Prob_link: https://www.codingninjas.com/studio/problems/reverse-nodes-in-k-group_8230709?challengeSlug=striver-sde-challenge&leftPanelTab=0

from math import *
from collections import *
from sys import *
from os import *


# Following is the class structure of the Node class:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def helper(head, index, n, block):
    # if "head" is None or "index" is >= length of block "n"
    # returning the head as it need not be reversed
    if head is None or index >= n:
        return head
    count = 0
    current_el = head
    prev_el = None
    next_el = None
    while current_el and count < block[index]:
        next_el = current_el.next
        # changing the direction of the link
        current_el.next = prev_el
        # setting "current_el" element as "prev_el" and
        # "next_el" element as "current_el" and "count"
        # is incremented by 1 for next iteration
        prev_el = current_el
        current_el = next_el
        count += 1

    # if "next_el" is not None, index is incremented by 1
    # and recursive call is made
    if next_el:
        index += 1
        # skipping recursive call if the block element is "0"
        # and next block element is taken incrementally
        while index < n and block[index] == 0:
            index += 1

        head.next = helper(next_el, index, n, block)
    # returning the reversed linked list
    return prev_el


def getListAfterReverseOperation(head, n, block):
    # if "block" has a single element and it is "<= 1"
    # returning "head" as no reversal need to made
    if n == 1 and block[0] <= 1:
        return head
    return helper(head, 0, n, block)
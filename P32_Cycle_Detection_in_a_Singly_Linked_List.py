# Prob_link: https://www.codingninjas.com/codestudio/problems/cycle-detection-in-a-singly-linked-list_8230683?challengeSlug=striver-sde-challenge&leftPanelTab=0

'''
Following is the structure of the Node class already defined.

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
'''


def detectCycle(head):
    # Write your code here.
    first = head
    second = head
    if head is None:
        return False
    while (second != None and second.next != None):
        first = first.next
        second = second.next.next
        if first == second:
            return True

    return False
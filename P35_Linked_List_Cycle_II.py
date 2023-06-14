# prob_link: https://www.codingninjas.com/codestudio/problems/linked-list-cycle-ii_8230823?challengeSlug=striver-sde-challenge&leftPanelTab=0

'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


def firstNode(head):
    # Write your code here
    temp = head
    seen = set()
    while (temp):
        if temp in seen:
            return temp

        seen.add(temp)
        temp = temp.next
    return None

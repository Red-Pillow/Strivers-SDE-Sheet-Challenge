# code_link: https://www.codingninjas.com/codestudio/problems/delete-kth-node-from-end_8230725?challengeSlug=striver-sde-challenge&leftPanelTab=0

'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


def removeKthNode(head, n):
    q = head
    length = 0
    while (q):
        length += 1
        q = q.next

    from_first = length - n
    if head is None:
        return head
    elif from_first == 0:
        head = head.next
        return head
    else:
        i = 0
        second = head
        while (second):
            i += 1
            if i == from_first:
                second.next = second.next.next
                break
            second = second.next
        return head

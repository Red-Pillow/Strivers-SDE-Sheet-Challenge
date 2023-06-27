# prob_link: https://www.codingninjas.com/studio/problems/intersection-of-two-linked-lists_8230688?challengeSlug=striver-sde-challenge&leftPanelTab=0

'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


def findIntersection(firstHead, secondHead):
    st = set()
    temp = firstHead
    while (temp):
        st.add(temp)
        temp = temp.next
    temp = secondHead
    while (temp):
        if temp in st:
            return temp
        temp = temp.next


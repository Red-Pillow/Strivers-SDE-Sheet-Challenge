# prob_link: https://www.codingninjas.com/studio/problems/add-two-numbers-as-linked-lists_8230833?challengeSlug=striver-sde-challenge&leftPanelTab=0

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    # Write your code here.
    temp1 = head1
    temp2 = head2
    summ = 0
    carry = 0
    prev = temp1
    while (temp1 != None and temp2 != None):
        summ = temp1.data + temp2.data + carry
        if summ > 9:
            carry = 1
        else:
            carry = 0
        temp1.data = summ % 10
        temp2.data = summ % 10
        prev = temp1
        temp1 = temp1.next
        temp2 = temp2.next
        summ = 0

    summ = 0
    flag = "both"
    while (temp2 != None):
        flag = "temp2"
        summ = temp2.data + carry
        if summ > 9:
            carry = 1
        else:
            carry = 0
        temp2.data = summ % 10
        prev = temp2
        temp2 = temp2.next

        summ = 0

    summ = 0
    while (temp1 != None):
        flag = "temp1"
        summ = temp1.data + carry
        if summ > 9:
            carry = 1
        else:
            carry = 0
        temp1.data = summ % 10
        prev = temp1
        temp1 = temp1.next
        summ = 0
    if carry != 0:
        if flag == "temp2":
            q = Node(carry)
            prev.next = q
        else:
            p = Node(carry)
            prev.next = p

    if flag == "both" or flag == "temp1":
        return head1
    else:
        return head2
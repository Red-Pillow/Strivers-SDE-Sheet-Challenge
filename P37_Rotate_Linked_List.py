# prob_link: https://www.codingninjas.com/studio/problems/rotate-linked-list_8230752?challengeSlug=striver-sde-challenge&leftPanelTab=0

class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next


def rotate(head: Node, k: int) -> Node:
    # Write your code here.
    ans = []
    temp = head
    while(temp):
        ans.append(temp.data)
        temp = temp.next
    if not ans:
        return head
    k = k%len(ans)
    ans = ans[-k:]+ans[:-k]
    c = 0
    temp = head
    while(temp):
        temp.data = ans[c]
        temp = temp.next
        c+=1
    return head

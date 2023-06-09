# Prob_link: https://www.codingninjas.com/codestudio/problems/single-element-in-a-sorted-array_8230826?challengeSlug=striver-sde-challenge&leftPanelTab=0

def singleNonDuplicate(arr):
    # Write your code here
    xor = 0
    for x in arr:
        xor^=x
    return xor


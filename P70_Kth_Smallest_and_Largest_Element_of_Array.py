# Prob_link: https://www.codingninjas.com/codestudio/problems/kth-smallest-and-largest-element-of-array_8230829?challengeSlug=striver-sde-challenge&leftPanelTab=0
def kthSmallLarge(arr, n, k):
    # Write your code here
    arr.sort()
    k-=1
    return [arr[k],arr[-k-1]]


# prob_link: https://www.codingninjas.com/codestudio/problems/find-duplicate-in-array_8230816?challengeSlug=striver-sde-challenge&leftPanelTab=0

def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    p = [0]*(n+1)
    for x in arr:
        p[x]+=1
        if p[x]>1:
            return x
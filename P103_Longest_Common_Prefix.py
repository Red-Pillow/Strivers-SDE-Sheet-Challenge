# prob_link: https://www.codingninjas.com/studio/problems/longest-common-prefix_8230847?challengeSlug=striver-sde-challenge&leftPanelTab=0

def longestCommonPrefix(A, n):
    # Write your code here
    # Return a string

    if len(A) == 0:
        return ""
    mini = 100000000
    for i in range(len(A)):
        mini = min(mini, len(A[i]))

    c = 0
    for i in range(mini):
        mp = {}
        for j in range(len(A)):
            if A[j][i] not in mp:
                mp[A[j][i]] = 1
            else:
                mp[A[j][i]] += 1
        if mp[A[j][i]] != len(A):
            break
        else:
            c += 1
    return (A[0][:c])


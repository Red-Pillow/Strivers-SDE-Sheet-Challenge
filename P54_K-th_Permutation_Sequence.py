# prob_link: https://www.codingninjas.com/codestudio/problems/k-th-permutation-sequence_8230822?challengeSlug=striver-sde-challenge&leftPanelTab=0

def kthPermutation(n, k):
    # Write your code here.
    k -= 1

    new, factorials = '', [1]
    for i in range(1, 1 + n):
        new = new + str(i)
        if i >= 2 and i < n:
            factorials.append(i * factorials[-1])

    def dfs(current, remaining, k):
        if len(remaining) <= 1: return current + remaining
        idx = k // factorials[-1]

        current = current + remaining[idx]
        k -= idx * factorials.pop()
        return dfs(current, remaining[:idx] + remaining[idx + 1:], k)

    return dfs('', new, k)

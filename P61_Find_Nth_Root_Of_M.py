# prob_link: https://www.codingninjas.com/codestudio/problems/find-nth-root-of-m_8230799?challengeSlug=striver-sde-challenge&leftPanelTab=0

def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    low = 0
    high = m
    ans = -1
    while (low <= high):
        mid = low + (high - low) // 2
        if mid ** n <= m:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    if ans ** n == m:
        return ans

    return -1
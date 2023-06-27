# prob_link: https://www.codingninjas.com/studio/problems/day-29-k-max-sum-combinations_8230768?challengeSlug=striver-sde-challenge&leftPanelTab=0


def kMaxSumCombination(a, b, n, k):
    # Write your code here.
    a.sort(reverse=True)
    b.sort(reverse=True)
    from heapq import heapify, heappop, heappush
    i = 0
    j = 0
    n = len(a)
    m = len(b)
    hip = []
    heapify(hip)

    temp = (i, j)
    heappush(hip, [-(a[0] + b[0]), temp])

    seen = set()
    seen.add((i, j))

    ans = []
    while (k):
        summ, temp = heappop(hip)
        i = temp[0]
        j = temp[1]
        ans.append(-summ)
        if i + 1 < n:
            newsumm = a[i + 1] + b[j]
            temp1 = (i + 1, j)
            if temp1 not in seen:
                heappush(hip, [-newsumm, temp1])
                seen.add(temp1)

        if j + 1 < m:
            newsumm = a[i] + b[j + 1]
            temp2 = (i, j + 1)
            if temp2 not in seen:
                heappush(hip, [-newsumm, temp2])
                seen.add(temp2)
        k -= 1
    return ans
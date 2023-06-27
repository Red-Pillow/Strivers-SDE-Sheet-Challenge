# prob_link: https://www.codingninjas.com/studio/problems/running-median_8230682?challengeSlug=striver-sde-challenge&leftPanelTab=0

def findMedian(arr, n):
    # Write your code here
    from sortedcontainers import SortedList
    slist = SortedList()
    ans = []
    for i in range(len(arr)):

        slist.add(arr[i])
        if i == 0:
            print(arr[i], end=" ")
            continue
        if len(slist) % 2 == 0:
            n = len(slist)
            print((slist[n // 2] + slist[(n // 2) - 1]) // 2, end=" ")
        else:
            n = len(slist)
            print(slist[n // 2], end=" ")
    print("")

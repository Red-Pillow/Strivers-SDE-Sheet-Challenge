# prob_link: https://www.codingninjas.com/studio/problems/median-in-a-stream_8230765?challengeSlug=striver-sde-challenge&leftPanelTab=0

def findMedian(nums, n):
    from sortedcontainers import SortedList
    arr = SortedList([])

    import math

    def findMedian():
        n = len(arr)
        if n%2==0:
            return math.floor((arr[n//2]+arr[(n//2)-1])/2)
        else:
            return arr[n//2]
    ans = []
    for i in range(len(nums)):
        arr.add(nums[i])
        ans.append(findMedian())

    return ans
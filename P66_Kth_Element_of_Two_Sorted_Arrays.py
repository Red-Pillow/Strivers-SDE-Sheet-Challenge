# prob_link: https://www.codingninjas.com/codestudio/problems/kth-element-of-two-sorted-arrays_8230824?challengeSlug=striver-sde-challenge&leftPanelTab=0

def ninjaAndLadoos(row1, row2, m, n, k):
    # Write your code here.
    def my_lower_bound(nums, target):
        low = 0
        high = len(nums) - 1
        ans = -1
        while (low <= high):
            mid = low + (high - low) // 2
            if nums[mid] <= target:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        if ans != -1:
            count = (ans + 1)
        else:
            count = 0
        return [count, nums[ans]]

    def send(mid):
        cnt1, val1 = my_lower_bound(row1, mid)
        cnt2, val2 = my_lower_bound(row2, mid)
        if cnt1 == 0:
            return [cnt2 <= k, cnt2, val2]
        if cnt2 == 0:
            return [cnt1 <= k, cnt1, val1]

        return [cnt1 + cnt2 <= k, cnt1 + cnt2, max(val1, val2)]

    low = min(min(row1), min(row2))
    high = max(max(row1), max(row2))
    ans = 0
    while (low <= high):
        mid = low + (high - low) // 2
        flag, cnt, val = send(mid)
        if flag == True:
            ans = val
            low = mid + 1
        else:
            high = mid - 1

    flag1, cnt1, val1 = send(ans)
    flag2, cnt2, val2 = send(ans + 1)

    if cnt1 == k:
        ans = val1
    else:
        ans = val2
    return ans
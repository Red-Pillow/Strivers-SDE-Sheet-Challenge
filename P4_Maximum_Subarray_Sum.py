# prob_link: https://www.codingninjas.com/codestudio/problems/maximum-subarray-sum_8230694?challengeSlug=striver-sde-challenge&leftPanelTab=0

def maxSubarraySum(nums, n):
    summ = 0
    maxi = 0
    for i in range(len(nums)):
        if summ <= 0:
            summ = 0
        summ += nums[i]
        maxi = max(maxi, summ)

    return maxi
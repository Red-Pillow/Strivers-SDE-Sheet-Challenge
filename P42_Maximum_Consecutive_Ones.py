# Prob_link: https://www.codingninjas.com/codestudio/problems/maximum-consecutive-ones_8230736?challengeSlug=striver-sde-challenge&leftPanelTab=0

def longestSubSeg(nums, n, k):
    #   Write your code here.

    left = 0
    total_ones = 0
    total_zeros = 0
    maxi = 0
    for right in range(len(nums)):
        if nums[right] == 1:
            total_ones += 1
        else:
            total_zeros += 1

        while (total_zeros > k):
            if nums[left] == 0:
                total_zeros -= 1
            else:
                total_ones -= 1

            left += 1

        maxi = max(maxi, total_ones + total_zeros)
    return maxi



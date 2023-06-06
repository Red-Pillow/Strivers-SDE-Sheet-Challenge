# Prob_link: https://www.codingninjas.com/codestudio/problems/longest-subarray-zero-sum_8230747?challengeSlug=striver-sde-challenge&leftPanelTab=0

def LongestSubsetWithZeroSum(nums):

    # Write your Code here.
    # Return an integer denoting the answer.
    mp = {0:-1}
    summ = 0
    ans = 0
    for i in range(len(nums)):
        summ+=nums[i]
        if summ in mp:
            ans = max(ans,i-mp[summ])
        else:
            mp[summ] = i
    return ans


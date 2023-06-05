# https://www.codingninjas.com/codestudio/problems/remove-duplicates-from-sorted-array_8230811?challengeSlug=striver-sde-challenge&leftPanelTab=0


def removeDuplicates(nums,n):
    # Write your code here.
    n = len(nums)
    i = 0
    j = 0
    while(j<n):
        if nums[i]==nums[j]:
            j+=1
        else:
            nums[i+1] = nums[j]
            i+=1
            j+=1
    return i+1
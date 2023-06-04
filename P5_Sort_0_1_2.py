# prob_link: https://www.codingninjas.com/codestudio/problems/sort-0-1-2_8230695?challengeSlug=striver-sde-challenge&leftPanelTab=0

def sort012(nums, n):
    # write your code here
    # don't return anything

    low = 0
    mid = 0
    high = len(nums) - 1
    while (mid <= high):
        if nums[mid] == 1:
            mid += 1
        elif nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
    return nums
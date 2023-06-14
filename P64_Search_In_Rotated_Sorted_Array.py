# prob_link: https://www.codingninjas.com/codestudio/problems/search-in-rotated-sorted-array_8230687?challengeSlug=striver-sde-challenge&leftPanelTab=0

def search(nums, target):
    # Write your code here.
    low = 0

    high = len(nums) - 1

    while low <= high:
        mid = (low + high) >> 1

        if nums[mid] == target:
            return mid

        elif nums[mid] >= nums[low]:

            if (target >= nums[low] and target < nums[mid]):
                high = mid - 1
            else:
                low = mid + 1
        else:

            if (target <= nums[high] and target > nums[mid]):
                low = mid + 1
            else:
                high = mid - 1
    return -1


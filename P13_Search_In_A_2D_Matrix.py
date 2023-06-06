# Prob_link: https://www.codingninjas.com/codestudio/problems/search-in-a-2d-matrix_8230773?challengeSlug=striver-sde-challenge

def searchMatrix(mat: [[int]], target: int) -> bool:
    # Write your code here.
    n = len(mat)
    m = len(mat[0])
    low=0
    high = n-1
    ans = -1
    while(low<=high):
        mid = low+(high-low)//2
        if mat[mid][0]<=target:
            ans = mid
            low=mid+1
        else:
            high = mid-1

    if ans==-1:
        return (False)
    row = ans
    low = 0
    high = len(mat[0])-1
    while(low<=high):
        mid = low+(high-low)//2
        if mat[row][mid]<=target:
            ans = mid
            low = mid+1
        else:
            high= mid-1

    if mat[row][ans]==target:
        return (True)
    return False



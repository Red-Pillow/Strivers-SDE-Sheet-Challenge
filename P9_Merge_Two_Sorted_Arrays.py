# prob_link: https://www.codingninjas.com/codestudio/problems/merge-two-sorted-arrays_8230835?challengeSlug=striver-sde-challenge&leftPanelTab=0

def ninjaAndSortedArrays(nums1,nums2,m,n):
    # Write your code here.
    k=m+n-1
    while m>0 and  n>0:
        if nums1[m-1] > nums2[n-1]:
            nums1[k]=nums1[m-1]
            m-=1
        else:
            nums1[k]=nums2[n-1]
            n-=1
        k-=1
    while n>0:
        nums1[k]=nums2[n-1]
        n-=1
        k-=1
    return nums1
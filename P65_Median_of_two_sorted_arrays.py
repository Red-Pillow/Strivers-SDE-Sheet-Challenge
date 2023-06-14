# prob_link: https://www.codingninjas.com/codestudio/problems/median-of-two-sorted-arrays_8230788?challengeSlug=striver-sde-challenge&leftPanelTab=0

def median(nums1: int, nums2: int) -> float:
    # Write the function here.

    p = sorted(nums1 + nums2)
    if len(p) % 2 == 0:
        median = (p[int(len(p) / 2)] + p[int(len(p) / 2) - 1]) / 2
    else:
        median = p[int(len(p) / 2)]
    return float(median)
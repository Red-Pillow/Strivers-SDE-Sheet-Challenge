# prob_link: https://www.codingninjas.com/studio/problems/maximum-product-subarray_8230828?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

def maximumProduct(nums, n):
    # write your code here
    # Return an integer denoting the answer to the required problem
    for i in range(len(nums)):
        if i==0:
            maxsub = nums[0]
            minsub = nums[0]
            maxproductsub = nums[0]
            continue
        if nums[i]<0:
            minsub,maxsub = maxsub,minsub
        maxsub = max(maxsub*nums[i],nums[i])
        minsub = min(minsub*nums[i],nums[i])
        maxproductsub = max(maxproductsub,maxsub)
    return maxproductsub



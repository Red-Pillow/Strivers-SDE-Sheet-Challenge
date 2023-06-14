# prob_link: https://www.codingninjas.com/codestudio/problems/trapping-rain-water_8230693?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

def getTrappedWater(height, n) :
	# Write your code here.
	n = len(height)
	pre = [0]*n
	suff = [0]*n
	for i in range(len(height)):
		if i==0:
			pre[i]=height[0]
			continue
		pre[i]=max(pre[i-1],height[i])


	n = len(height)
	for i in range(len(height)-1,-1,-1):
		if i==n-1:
			suff[i] = height[-1]
			continue
		suff[i]=max(suff[i+1],height[i])
	ans = 0
	#suff = suff[::-1]
	for i in range(1,len(suff)-1):
		mini = min(suff[i],pre[i])
		ans += mini - height[i]
	return ans
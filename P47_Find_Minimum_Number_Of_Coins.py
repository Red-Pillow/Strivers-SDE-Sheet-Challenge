# Prob_link: https://www.codingninjas.com/codestudio/problems/find-minimum-number-of-coins_8230766?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
	denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
	denominations.sort(reverse = True)
	count = 0
	i = 0
	while(i<len(denominations)):
		if amount>=denominations[i]:
			amount-=denominations[i]
			count+=1
		else:
			i+=1
	return count

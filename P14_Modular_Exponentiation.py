# Prob_link:https://www.codingninjas.com/codestudio/problems/modular-exponentiation_8230803?challengeSlug=striver-sde-challenge&leftPanelTab=0


from math import *
from collections import *
from sys import *
from os import *

import sys
sys.setrecursionlimit(10**7)

def modularExponentiation(a, b, m):
	# Write your code here.
	ans = 1
	while(b):
		if b&1:
			ans = (ans*a)%m
		a = (a*a)%m
		b>>=1
	return ans
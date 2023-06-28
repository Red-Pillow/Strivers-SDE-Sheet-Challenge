# prob_link: https://www.codingninjas.com/studio/problems/check-permutation_8230834?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

def areAnagram(s, t):
    # Write your code here.
    return sorted(s)==sorted(t)
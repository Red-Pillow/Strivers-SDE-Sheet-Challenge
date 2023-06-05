# prob_link: https://www.codingninjas.com/codestudio/problems/longest-substring-without-repeating-characters_8230684?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

def uniqueSubstrings(s ) :
    # Write your code here.
    mp = {}
    left = 0
    maxi = 0
    for i in range(len(s)):
        if s[i] not in mp:
            mp[s[i]] = i
        else:
            while(s[i] in mp):
                del mp[s[left]]
                left+=1
            mp[s[i]]=i
        maxi = max(maxi,len(mp))
    return maxi
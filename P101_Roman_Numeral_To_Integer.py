# prob_link: https://www.codingninjas.com/studio/problems/roman-numeral-to-integer_8230780?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

def romanToInt(s):

    # Write your code here
    # Return the int value

    mp={}
    mp['I']=1
    mp['V']=5
    mp['X']=10
    mp['L']=50
    mp['C']=100
    mp['D']=500
    mp['M']=1000

    s=s[::-1]
    p=0
    p=p+mp[s[0]]
    for i in range(1,len(s)):
        if mp[s[i]]<mp[s[i-1]]:
            p=p-mp[s[i]]
        else:
            p+=mp[s[i]]
    return p
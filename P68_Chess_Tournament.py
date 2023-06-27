# prob_link: https://www.codingninjas.com/studio/problems/chess-tournament_8230779?challengeSlug=striver-sde-challenge&leftPanelTab=0



from os import *
from sys import *
from collections import *
from math import *

def chessTournament(positions, n , c):
    positions.sort()
    def func(mid):
        count = 1
        prev = positions[0]
        for i in range(len(positions)):
            if prev+mid<=positions[i]:
                count+=1
                prev = positions[i]
        return count
    low =1
    high = positions[-1]-positions[0]
    while(low<=high):
        mid = low+(high-low)//2
        if func(mid)>=c:
            ans = mid
            low = mid+1
        else:
            high = mid-1
    return ans
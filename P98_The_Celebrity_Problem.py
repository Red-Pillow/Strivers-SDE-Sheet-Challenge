# prob_link: https://www.codingninjas.com/studio/problems/the-celebrity-problem_8230781?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

'''
    This is signature of helper function 'knows'.
    You should not implement it, or speculate about its implementation.

    def knows(int A, int B); 
    Function 'knows(A, B)' will returns "true" if the person having
    id 'A' knows the person having id 'B' in the party, "false" otherwise.
'''

def findCelebrity(n, knows):

    # Write your code here.
    i=0
    j=n-1
    while i<j:
        if knows(i,j):
            i+=1
        else:
            j-=1

    ## i is my answer revalidate my answer
    for A in range(n):
        if A!=i and (knows(A,i)==False or knows(i,A)):
            return -1
    return i


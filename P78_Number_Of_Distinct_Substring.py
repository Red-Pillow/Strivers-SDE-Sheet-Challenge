# prob_link: https://www.codingninjas.com/studio/problems/number-of-distinct-substring_8230842?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *


def distinctSubstring(str):
    # Write your code here.
    result = set()

    # List All Substrings
    for i in range(len(str) + 1):
        for j in range(i + 1, len(str) + 1):
            # Add each substring in Set
            result.add(str[i:j]);
        # Return size of the HashSet
    return len(result);


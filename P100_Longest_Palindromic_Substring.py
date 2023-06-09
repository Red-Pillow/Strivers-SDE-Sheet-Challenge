# Prob_link: https://www.codingninjas.com/codestudio/problems/day-12-longest-palindromic-substring_8230702?challengeSlug=striver-sde-challenge&leftPanelTab=0

def longestPalinSubstring(s):

    # Write your code here.
    def check_pallin(s,l,r):
        while(l>=0 and r<len(s) and s[r]==s[l]):
            l-=1
            r+=1
        return s[l+1:r]


    maxi = 0
    ans = ""
    n = len(s)
    for i in range(len(s)):
        odd = check_pallin(s,i,i)
        even = check_pallin(s,i,i+1)

        if len(odd)>maxi:
            maxi = len(odd)
            ans = odd

        if len(even)>maxi:
            maxi = len(even)
            ans = even
    return ans

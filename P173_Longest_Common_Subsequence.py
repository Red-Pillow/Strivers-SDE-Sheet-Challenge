# prob_link: https://www.codingninjas.com/studio/problems/longest-common-subsequence_8230681?challengeSlug=striver-sde-challenge&leftPanelTab=0


from sys import stdin


def lcs(text1, text2):
    # Your code goes here
    n = len(text1)
    m = len(text2)
    mp = {}

    def recur(text1, text2, n, m):
        if n == 0 or m == 0:
            return 0
        if (n, m) in mp:
            return mp[(n, m)]
        if text1[n - 1] == text2[m - 1]:
            mp[(n, m)] = 1 + recur(text1, text2, n - 1, m - 1)
        else:
            mp[(n, m)] = max(recur(text1, text2, n, m - 1), recur(text1, text2, n - 1, m))
        return mp[(n, m)]

    return recur(text1, text2, n, m)


# main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))


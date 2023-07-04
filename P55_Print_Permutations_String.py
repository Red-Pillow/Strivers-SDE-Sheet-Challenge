# prob_link: https://www.codingninjas.com/studio/problems/day-13-print-permutations-string_8230703?challengeSlug=striver-sde-challenge&leftPanelTab=0


def findPermutations(s):
    # Write your code here.
    def permute(s, answer):
        if (len(s) == 0):
            res.append(answer)
            return

        for i in range(len(s)):
            ch = s[i]
            left_substr = s[0:i]
            right_substr = s[i + 1:]
            rest = left_substr + right_substr
            permute(rest, answer + ch)

    answer = ""
    res = []
    permute(s, answer)
    return res
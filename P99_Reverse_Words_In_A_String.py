# Prob_link: https://www.codingninjas.com/codestudio/problems/reverse-words-in-a-string_8230698?challengeSlug=striver-sde-challenge&leftPanelTab=0

def reverseString(s: str) -> str:
    # Write your code from here.
    word = []
    s += " "
    temp = ""
    for i in range(len(s)):
        if s[i] != " ":
            temp += s[i]
        else:
            word.append(temp)
            temp = ""

    res = []
    for i in range(len(word)):
        if len(word[i]) != 0:
            res.append(word[i])
    word = res[::-1]
    ans = ""
    for i in range(len(word)):
        ans += word[i]
        ans += " "
    if not ans:
        return ans
    if ans[-1] == ' ':
        ans = ans[:-1]
    return ans

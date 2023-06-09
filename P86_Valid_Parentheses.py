# Prob_link: https://www.codingninjas.com/codestudio/problems/valid-parentheses_8230714?challengeSlug=striver-sde-challenge&leftPanelTab=0

def isValidParenthesis(s):
    # Write your code here.
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
            continue

        if (stack[-1] == '(' and s[i] == ')') or (stack[-1] == '{' and s[i] == '}') or (
                stack[-1] == '[' and s[i] == ']'):
            stack.pop()
        else:
            stack.append(s[i])
    return len(stack) == 0


# Main Code

t = int(input().strip())

for i in range(t):
    str = input().strip()
    ans = isValidParenthesis(str)

    if ans:
        print("Balanced")

    else:
        print("Not Balanced")

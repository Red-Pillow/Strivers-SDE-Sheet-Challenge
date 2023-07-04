# prob_link: https://www.codingninjas.com/studio/problems/online-stock-span_8230843?challengeSlug=striver-sde-challenge&leftPanelTab=0


def findSpans(price):
    res = [1] * len(price)
    stack = []
    for idx, p in enumerate(price):
        while stack and p >= price[stack[-1]]:
            stack.pop()

        res[idx] = (idx - stack[-1]) if stack else (idx + 1)
        stack.append(idx)
    return res
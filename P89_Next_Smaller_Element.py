# prob_link: https://www.codingninjas.com/studio/problems/next-smaller-element_8230814?challengeSlug=striver-sde-challenge&leftPanelTab=0

def nextSmallerElement(arr, n):
    # Write your code here.
    n = len(arr)

    stack = [-1]

    ans = [0] * n

    for i in range(n - 1, -1, -1):

        while stack and stack[-1] >= arr[i]:
            stack.pop()

        ans[i] = stack[-1]

        stack.append(arr[i])

    return ans
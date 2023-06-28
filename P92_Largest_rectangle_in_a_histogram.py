# prob_link: https://www.codingninjas.com/studio/problems/largest-rectangle-in-a-histogram_8230792?challengeSlug=striver-sde-challenge&leftPanelTab=0

def largestRectangle(heights):
    # Write your code here.
    A = heights
    if len(A) == 0:
        return 0

    def right_left(A):
        vec = []
        stack = []
        vec.append(invalid_no)
        stack.append([A[-1], len(A) - 1])
        for i in range(len(A) - 2, -1, -1):
            if len(stack) == 0:
                vec.append(invalid_no)
            elif len(stack) > 0:
                if stack[-1][0] < A[i]:
                    vec.append(stack[-1][1])
                else:
                    while (len(stack) > 0 and stack[-1][0] >= A[i]):
                        stack.pop()
                    if len(stack) == 0:
                        vec.append(invalid_no)
                    else:
                        vec.append(stack[-1][1])
            stack.append([A[i], i])
        return vec[::-1]

    invalid_no = len(A)
    smallest_right = right_left(A)

    A_rev = A[::-1]
    invalid_no = -1
    smallest_left = right_left(A_rev)

    k = len(A) - 1

    for i in range(len(smallest_left)):
        if smallest_left[i] != -1:
            smallest_left[i] = k - smallest_left[i]

    smallest_left = smallest_left[::-1]

    maxi = 0
    for i in range(len(A)):
        maxi = max(maxi, (smallest_right[i] - smallest_left[i] - 1) * A[i])
    return maxi
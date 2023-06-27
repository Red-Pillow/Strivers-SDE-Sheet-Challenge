# prob_link: https://www.codingninjas.com/studio/problems/matrix-median_8230735?challengeSlug=striver-sde-challenge&leftPanelTab=0

def getMedian(matrix):
    # Write your code here.
    p = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            p.append(matrix[i][j])
    p.sort()
    n = len(p)//2
    if len(p)%2==0:
        return p[n]+p[n-1]
    return p[n]

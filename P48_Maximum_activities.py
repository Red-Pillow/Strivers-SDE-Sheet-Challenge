# Prob_link: https://www.codingninjas.com/codestudio/problems/maximum-activities_8230800?challengeSlug=striver-sde-challenge&leftPanelTab=0

def maximumActivities(start, finish):
    # Write your Code here.
    n = len(start)
    aux = []
    for i in range(n):
        aux.append([finish[i],start[i]])
    aux.sort()
    count = 1
    endl = aux[0][0]
    for i in range(1,n):
        s = aux[i][1]
        e = aux[i][0]

        if s>=endl:
            count+=1
            endl = e

    return count


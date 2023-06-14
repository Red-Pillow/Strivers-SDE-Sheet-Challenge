# prob_link: https://www.codingninjas.com/codestudio/problems/job-sequencing-problem_8230832?challengeSlug=striver-sde-challenge&leftPanelTab=0
def jobScheduling(jobs):
    maxi = 0
    for t, profit in jobs:
        maxi = max(maxi, t)
    maxi += 1
    flag = [0] * maxi
    jobs.sort(key=lambda x: x[1], reverse=True)
    for t, profit in jobs:
        for starts in range(t, 0, -1):
            if flag[starts] == 0:
                flag[starts] = profit
                break  #
    return sum(flag)


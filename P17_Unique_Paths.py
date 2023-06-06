# Prob_link: https://www.codingninjas.com/codestudio/problems/reverse-pairs_8230825?challengeSlug=striver-sde-challenge&leftPanelTab=0


def uniquePaths(n, m):
    # Write your code here.

    mp = {}

    def dfs(i, j):
        if i >= n or j >= m or i < 0 or j < 0:
            return 0
        if i == n - 1 and j == m - 1:
            return 1
        if (i, j) in mp:
            return mp[(i, j)]

        mp[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)

        return mp[(i, j)]

    return dfs(0, 0)

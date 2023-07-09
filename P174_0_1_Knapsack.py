# Prob_link: https://www.codingninjas.com/studio/problems/0-1-knapsack_8230801?challengeSlug=striver-sde-challenge&leftPanelTab=0

def maxProfit(values, weights, n, w):
    def memoization(idx, w, dp):
        if idx < 0 or w <= 0:
            return 0

        if dp[idx][w] != -1:
            return dp[idx][w]

        not_take = 0 + memoization(idx - 1, w, dp)

        take = float('-inf')
        if weights[idx] <= w:
            take = values[idx] + memoization(idx - 1, w - weights[idx], dp)

        dp[idx][w] = max(not_take, take)
        return dp[idx][w]

    def tabulation():
        dp = [[0] * (w + 1) for _ in range(n + 1)]

        for idx in range(1, n + 1):
            for W in range(1, w + 1):
                not_take = dp[idx - 1][W]

                take = 0
                if weights[idx - 1] <= W:
                    take = values[idx - 1] + dp[idx - 1][W - weights[idx - 1]]

                dp[idx][W] = max(not_take, take)

        return dp[n][w]

    # For memoization
    # dp = [[-1]*(w+1) for _ in range(n)]
    # return memoization(n-1,w,dp)

    # For tabulation
    return tabulation()
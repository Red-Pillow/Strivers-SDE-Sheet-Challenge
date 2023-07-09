# Prob_link: https://www.codingninjas.com/studio/problems/matrix-chain-multiplication_8230769?challengeSlug=striver-sde-challenge&leftPanelTab=0

def matrixMultiplication(arr, n):
    def memoization(i, j, dp):
        if i == j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        mini = float('inf')

        # Perform partition k inbtw idx 1 to n-1
        for k in range(i, j):
            steps = arr[i - 1] * arr[k] * arr[j]  # no of operations to multiply mat i - j
            steps += memoization(i, k, dp)  # best no of operations to multiply mat i - k
            steps += memoization(k + 1, j, dp)  # best no of operations to multiply mat k+1 - j

            # store minimum cost
            if steps < mini:
                mini = steps

        dp[i][j] = mini
        return dp[i][j]

    def tabulation():
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n, 1):
                mini = float('inf')

                for k in range(i, j):
                    steps = arr[i - 1] * arr[k] * arr[j] + dp[i][k] + dp[k + 1][
                        j]  # best no of operations to multiply mat k+1 - j

                    if steps < mini:
                        mini = steps

                dp[i][j] = mini

        return dp[i][j]

    # For memoization
    # dp = [ [-1]*n for _ in range(n) ]
    # return memoization(1,n-1,dp)

    # For tabulation
    return tabulation()
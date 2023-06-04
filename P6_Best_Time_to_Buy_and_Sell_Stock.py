# code_link: https://www.codingninjas.com/codestudio/problems/best-time-to-buy-and-sell-stock_8230746?challengeSlug=striver-sde-challenge&leftPanelTab=0

def maximumProfit(prices):
    # Write your code here.
    mini = prices[0]
    maxi = 0
    for i in range(len(prices)):
        if prices[i]-mini>=0:
            maxi = max(maxi,prices[i]-mini)
        mini = min(mini,prices[i])
    return maxi
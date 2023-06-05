# prob_link: https://www.codingninjas.com/codestudio/problems/missing-and-repeating-numbers_8230733?challengeSlug=striver-sde-challenge&leftPanelTab=0

def missingAndRepeating(nums, n):
    # Write your code here

    n = len(nums)
    should_be_summ = n * (n + 1) // 2
    now_summ = sum(nums)

    now_square_sum = 0
    for x in nums:
        now_square_sum += x ** 2
    should_be_square_sum = n * (n + 1) * (2 * n + 1) // 6

    val1 = now_summ - should_be_summ
    val2 = now_square_sum - should_be_square_sum
    val2 = val2 // val1
    x = (val1 + val2) // 2
    y = x - val1
    return [y, x]
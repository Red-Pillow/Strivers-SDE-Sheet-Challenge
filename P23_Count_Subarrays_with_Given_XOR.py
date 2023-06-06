# Prob_link: https://www.codingninjas.com/codestudio/problems/count-subarrays-with-given-xor_8230830?challengeSlug=striver-sde-challenge&leftPanelTab=0


def subarraysXor(nums, m):
    # Write your code here
    # Return an integer
    mp = {}
    xor = [nums[0]]
    ans = 0

    for i in range(1, len(nums)):
        xor.append(xor[-1] ^ nums[i])

    for i in range(len(nums)):
        temp = m ^ xor[i]
        if temp in mp:
            ans += mp[temp]

        if xor[i] == m:
            ans += 1
        if xor[i] not in mp:
            mp[xor[i]] = 1
        else:
            mp[xor[i]] = mp[xor[i]] + 1
    return ans
# Prob_link: https://www.codingninjas.com/codestudio/problems/combination-sum-ii_8230820?challengeSlug=striver-sde-challenge&leftPanelTab=0

def combinationSum2(candidates, n, target):
    # write your code here
    candidates.sort()
    n = len(candidates)

    def recur(index, target, arr, ds):
        if target == 0:
            ans.append(ds[:])
            return

        for i in range(index, len(arr)):
            if i > index and arr[i] == arr[i - 1]:
                continue

            if arr[i] > target:
                break
            ds.append(arr[i])
            recur(i + 1, target - arr[i], arr, ds)
            ds.pop()

    ans = []
    recur(0, target, candidates, [])
    return ans

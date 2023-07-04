# prob_link: https://www.codingninjas.com/studio/problems/return-subsets-sum-to-k_8230706?challengeSlug=striver-sde-challenge&leftPanelTab=0

def findSubsetsThatSumToK(arr, n, k):
    # Write your code here.
    def print_subsets_sum_to_k(arr, target):
        subsets = []
        generate_subsets(arr, 0, [], subsets, target)

        for subset in subsets:
            ans.append(subset)

    def generate_subsets(arr, index, current_subset, subsets, target):
        if index == len(arr):

            if sum(current_subset) == target:
                subsets.append(current_subset)
            return
        generate_subsets(arr, index + 1, current_subset, subsets, target)
        generate_subsets(arr, index + 1, current_subset + [arr[index]], subsets, target)

    ans = []

    print_subsets_sum_to_k(arr, k)
    return ans

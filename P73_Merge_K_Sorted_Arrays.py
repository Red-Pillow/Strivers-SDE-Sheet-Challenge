# prob_link: https://www.codingninjas.com/studio/problems/merge-k-sorted-arrays_8230770?challengeSlug=striver-sde-challenge&leftPanelTab=0


def mergeKSortedArrays(kArrays, k:int):
	# Write your code here.
	# kArrays is a list of 'k' lists.
	# Return a list.
	s = []
	for arr in kArrays:
		for x in arr:
			s.append(x)
	s.sort()
	return s


# prob_link: https://www.codingninjas.com/studio/problems/maximum-in-sliding-windows-of-size-k_8230772?challengeSlug=striver-sde-challenge&leftPanelTab=0



def slidingWindowMaximum(nums:list, k:int):
	# Write your code here
	# Return a list
	from collections import deque
	dq = deque()
	for i in range(k):
		if not dq:
			dq.append(i)
			continue
		while(dq and nums[dq[-1]]<nums[i]):
			dq.pop()
		dq.append(i)

	ans = []
	ans = [nums[dq[0]]]
	left = 1
	for right in range(k,len(nums)):
		while(dq and dq[0]<left):
			dq.popleft()
		while(dq and nums[dq[-1]]<nums[right]):
			dq.pop()
		dq.append(right)
		ans.append(nums[dq[0]])
		left+=1
	return ans
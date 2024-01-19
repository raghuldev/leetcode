class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = nums[0] < nums[-1]
        for i in range(1, len(nums)):
            if isIncreasing and not nums[i-1] <= nums[i]:
                return False
            elif not isIncreasing and not nums[i-1] >= nums[i]:
                return False
        return True

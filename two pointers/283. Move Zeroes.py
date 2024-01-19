class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == 0:
                nums.remove(0)
                nums.append(0)
            left += 1
        print(nums)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [num ** 2 for num in nums]
        return sorted(res)
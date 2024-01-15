class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for key, value in enumerate(nums1):
            under_line = nums2.index(value)
            swapped = False
            for i in range(under_line + 1, len(nums2)):
                if nums2[i] > nums2[under_line]:
                    nums1[key] = nums2[i]
                    swapped = True
                    break
            if not swapped:
                nums1[key] = -1
        return nums1



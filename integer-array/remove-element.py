class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        for num in nums:
            if num != val:
                nums[left] = num
                left += 1
        return left


solve = Solution()
print(solve.removeElement([3, 2, 2, 3], 3))

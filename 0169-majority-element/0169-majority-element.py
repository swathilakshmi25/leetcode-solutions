class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if not nums:
            return None
        nums.sort()
        return nums[len(nums) // 2]
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        total = 0

        for num in nums:
            total += maxi - num

        return total
        
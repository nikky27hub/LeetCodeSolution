class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = {}

        n = len(nums)

        for i in range(n - k + 1):
            for x in set(nums[i:i+k]):
                freq[x] = freq.get(x, 0) + 1

        ans = -1

        for x, count in freq.items():
            if count == 1:
                ans = max(ans, x)

        return ans
       
        
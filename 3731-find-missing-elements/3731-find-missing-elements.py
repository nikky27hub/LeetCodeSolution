class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn = min(nums)
        mx = max(nums)

        m= set(nums)
        return [x for x in range(mn+1,mx) if x  not in m]
        
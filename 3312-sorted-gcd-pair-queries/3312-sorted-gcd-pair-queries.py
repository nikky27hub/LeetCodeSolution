class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = Counter(nums)

        gcd_count = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            cnt = 0
            for multiple in range(g, mx + 1, g):
                cnt += freq[multiple]
                gcd_count[g] -= gcd_count[multiple]
            gcd_count[g] += cnt * (cnt - 1) // 2

        prefix = list(accumulate(gcd_count))

        return [bisect_right(prefix, q) for q in queries]
        
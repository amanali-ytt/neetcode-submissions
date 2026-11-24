class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        seen = {0:1} # Base case : prefix sum is 0 and seen once
        for num in nums:
            prefix_sum += num
            if (prefix_sum-k) in seen:
                count += seen[prefix_sum-k]
            seen[prefix_sum] = 1 + seen.get(prefix_sum, 0) 
        return count
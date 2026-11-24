class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res= Cursum = 0
        prefix_Sums = {0:1}
        for num in nums:
            Cursum += num
            diff = Cursum -k

            res += prefix_Sums.get(diff,0)
            prefix_Sums[Cursum] = 1+ prefix_Sums.get(Cursum,0)
        return res    
        
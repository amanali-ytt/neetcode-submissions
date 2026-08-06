from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Freq = Counter(nums)
        for value in Freq.values():
            if value > 1:
                return True
        return False
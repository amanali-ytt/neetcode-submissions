class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        sorted_num = nums
        n = len(sorted_num)
        for i in range(n-1):
            if sorted_num[i] == sorted_num[i+1]:
                return True
        return False
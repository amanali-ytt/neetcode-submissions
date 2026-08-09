class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0]*len(nums)
        if zero_count == 1:
            product = 1
            for num in nums:
                if num!= 0:
                    product *= num
        
            res = [0]*len(nums)
            zero_index = nums.index(0)
            res[zero_index] = product
            return res
        product = 1
        for num in nums:
            product *= num
        return [product//num for num in nums]       



        
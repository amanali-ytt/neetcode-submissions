class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = []
        post_sum = []
        window_left,window_right = 0,0 
        for i in range(len(nums)):
            window_left += nums[i]
            prefix_sum.append(window_left)
            window_right += nums[len(nums)-i-1]
            post_sum.append(window_right)
        post_sum.reverse()
        for i in range(len(nums)):
            if prefix_sum[i] == post_sum[i]:
                return i
        return -1        


            

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}                                      # hash map where value will be stored  to check afterwards 
        for i in range(len(nums)):                    # loop it in to whole set of len of array
            if nums[i] in mp and i - mp[nums[i]] <= k:   # check if ith element of array is in table along with position of it is with duplicate what position it is if it is less then k length then it is inside window
                return True
            mp[nums[i]] = i
        return False
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        res = []
        total = 0
        while left<right:
            total = numbers[left] + numbers[right]
            if total < target:
                left +=  1
            elif total > target:
                right -= 1
            else:
                res.append(left + 1)
                res.append(right + 1)
                return res
        return res
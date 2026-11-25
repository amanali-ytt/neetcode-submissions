# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        i,j = 0,len(nums)-1
        res = 0
        while i<j:
            res = max(res,nums[i] + nums[j])
            i,j = i+1,j-1
        return res
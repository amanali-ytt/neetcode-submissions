class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_nums = [c.lower() for c in s if c.isalnum()]
        return clean_nums[::] == clean_nums[::-1]
        
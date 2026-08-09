from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = Counter(nums)
        # Get the k elements with the highest frequencies
        return [item for item, count in freq_table.most_common(k)]
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                return True
        return False
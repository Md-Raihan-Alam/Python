# https://leetcode.com/problems/number-of-good-pairs
class Solution:
    pairs=0
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i=0
        while i < len(nums):
            j=i+1
            while j < len(nums):
                if nums[i]==nums[j]:
                    self.pairs=self.pairs+1
                j=j+1
            i=i+1
        return self.pairs
        
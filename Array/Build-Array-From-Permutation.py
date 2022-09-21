# https://leetcode.com/problems/build-array-from-permutation
class Solution:
    ans=list()
    def buildArray(self, nums: List[int]) -> List[int]:
        self.ans.clear()
        i=0
        while i < len(nums):
            self.ans.append(nums[nums[i]])
            i=i+1
        return self.ans
        
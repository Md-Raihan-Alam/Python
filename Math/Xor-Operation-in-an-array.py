# https://leetcode.com/problems/xor-operation-in-an-array
class Solution:
    ans=0
    def xorOperation(self, n: int, start: int) -> int:
        i=0
        self.ans=0
        nums=list()
        while i<n:
            nums.append((start+(2*i)))
            i=i+1
        for i in nums:
            self.ans=self.ans^i
        return self.ans
        
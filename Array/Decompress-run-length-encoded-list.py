# https://leetcode.com/problems/decompress-run-length-encoded-list
class Solution:
    decompressedList=[]
    temp=[]
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        self.temp.clear()
        self.decompressedList.clear()
        i=0
        while i<len(nums):
            self.temp.append(nums[i])
            if len(self.temp)==2:
                l=self.temp[0]
                n=self.temp[1]
                j=0
                while j<l:
                    self.decompressedList.append(n)
                    j=j+1
                self.temp.clear()
            i=i+1
        return self.decompressedList
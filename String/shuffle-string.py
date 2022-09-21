# https://leetcode.com/problems/shuffle-string
class Solution:
    final=""
    keyStr=dict()
    def restoreString(self, s: str, indices: List[int]) -> str:
        i=0
        self.keyStr.clear()
        self.final=""
        while i<len(s):
            self.keyStr[indices[i]]=s[i]
            i=i+1
        for i in sorted(self.keyStr):
            self.final=self.final+self.keyStr[i]
        return self.final
        
        
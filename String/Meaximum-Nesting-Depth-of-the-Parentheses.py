# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses
class Solution:
    deepBrac=0
    def maxDepth(self, s: str) -> int:
        i=0
        tempBrac=0
        self.deepBrac=0
        while i < len(s):
            if s[i]=='(':
                tempBrac=tempBrac+1
            elif s[i]==')':
                if tempBrac>self.deepBrac:
                    self.deepBrac=tempBrac
                tempBrac=tempBrac-1
            i=i+1
        return self.deepBrac
            
        
        
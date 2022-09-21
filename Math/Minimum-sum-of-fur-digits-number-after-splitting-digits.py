# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits
class Solution:
    minNum=0
    def minimumSum(self, num: int) -> int:
        self.minNum=0
        tempStr=str(num)
        digitStr=''.join(sorted(tempStr))
        firstPair=digitStr[0]+digitStr[2]
        secondPair=digitStr[1]+digitStr[3]
        pair=list()
        pair.append(int(firstPair))
        pair.append(int(secondPair))
        self.minNum+=pair[0]
        self.minNum+=pair[1]
        return self.minNum
        
        
# https://leetcode.com/problems/truncate-sentence
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        trunSen=""
        strList=s.split(" ")
        for i in range(0,k):
            trunSen+=strList[i]
            trunSen+=" "
        return trunSen.strip()
        
# class Solution:
#     def truncateSentence(self, s: str, k: int) -> str:
#         return ' '.join(s.split()[:k])
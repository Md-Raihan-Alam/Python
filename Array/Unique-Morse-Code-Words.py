# https://leetcode.com/problems/unique-morse-code-words
class Solution:
    diffTrans=set()
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        self.diffTrans.clear()
        alpaMarshCode={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        for i in words:
            temp=""
            for j in i:
                temp=temp+alpaMarshCode[j]
            self.diffTrans.add(temp)
        return len(self.diffTrans)


# class Solution:
#     def uniqueMorseRepresentations(self, words: List[str]) -> int:
#         morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#         hashset = set()
        
#         for word in words:
#             curr = []
#             for c in word:
#                 curr.append(morse[ord(c) - ord("a")])
#             hashset.add("".join(curr))
#         return len(hashset)

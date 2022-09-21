# https://leetcode.com/problems/decode-the-message
class Solution:
    keyMas=dict()
    ch='a'
    rm=""
    def decodeMessage(self, key: str, message: str) -> str:
        self.rm=""
        for i in key:
            if i!=' ' and i not in self.keyMas:
                self.keyMas[i]=self.ch
                self.ch=chr(ord(self.ch)+1)
                if self.ch=='{':
                    self.ch='a'
        for i in message:
            if i==' ':
                self.rm=self.rm+' '
            else:
                self.rm=self.rm+self.keyMas[i]
        self.keyMas.clear()
        self.ch='a'
        return self.rm
        
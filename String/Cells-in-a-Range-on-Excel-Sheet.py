# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet
class Solution:
    cells=list()
    def cellsInRange(self, s: str) -> List[str]:
        self.cells.clear()
        holdList=s.split(":")
        first=holdList[0][0:1]
        second=holdList[0][1:2]
        third=holdList[1][0:1]
        fourth=holdList[1][1:2]
        tempNum=second
        while True:
            newStr=str(first+second)
            self.cells.append(newStr)
            if first==third and second==fourth:
                break
            else:
                second=chr(ord(second)+1)
                if second > fourth:
                    second=tempNum
                    first=chr(ord(first)+1)
        return self.cells        
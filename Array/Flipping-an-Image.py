# https://leetcode.com/problems/flipping-an-image
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        output=list()
        for i in image:
            # print(i)
            # i.reverse()
            tempI=list()
            for j in i[::-1]:
                if j==0:
                    tempI.append(1)
                else:
                    tempI.append(0)
            output.append(tempI)
        return output
# https://www.lintcode.com/problem/813/
# https://leetcode.com/problems/find-anagram-mappings
from typing import (
    List,
)

class Solution:
    """
    @param a: lists A
    @param b: lists B
    @return: the index mapping
    """
    def anagram_mappings(self, a: List[int], b: List[int]) -> List[int]:
        # Write your code here
        output=list()
        for i in range(0,len(a)):
            for j in range(0,len(b)):
                if(a[i]==b[j]):
                        output.append(j)
                        break
        return output
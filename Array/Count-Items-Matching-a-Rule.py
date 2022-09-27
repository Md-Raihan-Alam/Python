# https://leetcode.com/problems/count-items-matching-a-rule
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        match=0
        if ruleKey=="type":
            j=0
            for i in range(len(items)):
                if items[i][j]==ruleValue:
                    match=match+1
        elif ruleKey=="color":
            j=1
            for i in range(len(items)):
                if items[i][j]==ruleValue:
                    match=match+1
        elif ruleKey=="name":
            j=2
            for i in range(len(items)):
                if items[i][j]==ruleValue:
                    match=match+1
        return match
        
    #     class Solution:
    # def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    #     if ruleKey == "type":
    #         ruleKey = 0
    #     elif ruleKey == "color":
    #         ruleKey = 1
    #     elif ruleKey == "name":
    #         ruleKey = 2
            
    #     count = 0
    #     for item in items:
    #         if item[ruleKey] == ruleValue:
    #             count += 1
    #     return count 
# https://leetcode.com/problems/largest-local-values-in-a-matrix
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        output=list()
        i=0
        while i < len(grid)-2:
            row=list()
            j=0
            while j < len(grid)-2:
                values=list()
                values.append(grid[i][j])
                values.append(grid[i][j+1])
                values.append(grid[i][j+2])
                values.append(grid[i+1][j])
                values.append(grid[i+1][j+1])
                values.append(grid[i+1][j+2])
                values.append(grid[i+2][j])
                values.append(grid[i+2][j+1])
                values.append(grid[i+2][j+2])
                mx=max(values)
                row.append(mx)
                j=j+1
            output.append(row)
            i=i+1
        return output
            
# good
# better solution
# class Solution:
    
#     def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
#         output = []
        
        
        
#         def getCube(i,j, grid):
#             if i < len(grid) and j < len(grid[i]):
#                 cube = [grid[i][j],grid[i][j+1],grid[i][j+2],grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]]
#                 return cube
#             else:
#                 return
#         # [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
        
#         temp = []
#         for i in range(len(grid) - 2):
#             for j in range(len(grid[i]) - 2):
#                 temp.append(max(getCube(i,j,grid)))
                
#             output.append(temp)
#             temp = []

        
#         return output
        
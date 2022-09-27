# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        move=0
        seats.sort()
        students.sort()
        i=0
        while i<len(seats):
            move=move+abs(seats[i]-students[i])
            i=i+1
        return move
        
# class Solution:
#     def minMovesToSeat(self, seats: List[int], students: List[int]) ->int:
#         students.sort()
#         seats.sort()
#         return sum(abs(seats[i]-students[i]) for i in range(len(seats)))
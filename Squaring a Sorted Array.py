# https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/squaring-a-sorted-array-easy
class Solution:
    def makeSquares(self, arr):
        squares = [x * x for x in arr]
        squares.sort()
        return squares

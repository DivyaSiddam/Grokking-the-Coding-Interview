# https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/contains-duplicate-easy
class Solution:
    def containsDuplicate(self, nums):
      return len(nums) != len(set(nums))
     

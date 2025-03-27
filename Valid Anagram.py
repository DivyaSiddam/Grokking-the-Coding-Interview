# https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/valid-anagram-easy
class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


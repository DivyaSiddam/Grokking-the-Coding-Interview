# https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/pair-with-target-sum-easy
class Solution:
    def search(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]

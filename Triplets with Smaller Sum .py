# https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/triplets-with-smaller-sum-medium
class Solution:
    def searchTriplets(self, arr, target):
        arr.sort()
        count = 0

        for i in range(len(arr) - 2):
            left = i + 1
            right = len(arr) - 1

            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                if current_sum < target:
                    # All triplets between left and right are valid
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count

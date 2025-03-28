# https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/triplet-sum-close-to-target-medium
class Solution:
    def searchTriplet(self, arr, target):
        arr.sort()
        closest = arr[0] + arr[1] + arr[2]  # Start with the first triplet

        for i in range(len(arr) - 2):
            left = i + 1
            right = len(arr) - 1

            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]

                # Update if closer, or same distance but smaller sum
                if abs(target - current_sum) < abs(target - closest) or \
                   (abs(target - current_sum) == abs(target - closest) and current_sum < closest):
                    closest = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest

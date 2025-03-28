# https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/find-nonduplicate-number-instances-easy
class Solution:
    def moveElements(self, arr):
        if len(arr) == 0:
            return 0

        unique_index = 1

        for i in range(1, len(arr)):
            if arr[i] != arr[unique_index - 1]:
                arr[unique_index] = arr[i]
                unique_index += 1

        return unique_index

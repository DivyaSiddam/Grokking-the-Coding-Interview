# https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/triplet-sum-to-zero-medium
class Solution:
  def searchTriplets(self, arr):
    triplets = []
    n = len(arr)

    for i in range(n):
      for j in range(i + 1, n):
        for k in range(j + 1, n):
          if arr[i] + arr[j] + arr[k] == 0:
            triplet = sorted([arr[i], arr[j], arr[k]])
            if triplet not in triplets:
              triplets.append(triplet)

    return triplets

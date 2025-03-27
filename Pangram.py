# https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/pangram-easy
class Solution:
    def checkIfPangram(self, sentence):
        sentence = sentence.lower()
        letters = set()

        for char in sentence:
            if char.isalpha():
                letters.add(char)

        return len(letters) == 26

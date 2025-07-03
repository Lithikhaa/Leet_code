class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()

        last = s[-1]
        lenght = len(last)
        return lenght
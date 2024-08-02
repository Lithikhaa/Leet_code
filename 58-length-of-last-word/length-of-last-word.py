class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        separte = s.split()


        return len(separte[-1])

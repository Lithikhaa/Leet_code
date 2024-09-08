class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        store = ' '.join(s[::-1])
        return store
        
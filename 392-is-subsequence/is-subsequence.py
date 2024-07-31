class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        l = len(s)
        c = 0
        if not s :
            return True
        for i in t :
            if i == s[c] :
                c += 1
            if c == l :
                break
        return l == c
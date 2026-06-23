class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""

        for i in range(len(strs[0])):
            reference = strs[0][i]

            for word in strs[1:]:
                if i >= len(word) or word[i] != reference:
                    return prefix

            prefix += reference

        return prefix
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        convert_str = str(x)
        if convert_str == convert_str[::-1]:
            return True
        else:
            return False

        
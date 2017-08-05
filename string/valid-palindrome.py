class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_index = 0
        right_index = len(s) - 1
        while left_index < right_index:
            if not s[left_index].isalnum():
                left_index += 1
                continue
            if not s[right_index].isalnum():
                right_index -= 1
                continue
            if s[left_index].lower() == s[right_index].lower():
                left_index += 1
                right_index -= 1
            else:
                return False

        return True

solve = Solution()
print(solve.isPalindrome("race a car"))

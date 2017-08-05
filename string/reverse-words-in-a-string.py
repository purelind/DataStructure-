class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(reversed(s.strip().split()))


solve = Solution()
print(solve.reverseWords( "the sky is blue"))

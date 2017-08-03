class Solution:
    """
    :param A: A string
    :param offset: Rotate string with offset.
    :return: Rotated string.
    """
    def rotateString(self, A, offset):
        if not A or len(A) == 0:
            return A

        offset %= len(A)
        before = A[:len(A) - offset]
        after = A[len(A) - offset:]
        A = before[::-1] + after[::-1]
        A = A[::-1]
        return A

solve = Solution()
print(solve.rotateString('abcdefg', 1))
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        originalNumber = x
        reversedNumber = 0
        while x > 0:
            remainder = x % 10
            reversedNumber = reversedNumber *10 + remainder
            x = x//10
        return originalNumber == reversedNumber
    
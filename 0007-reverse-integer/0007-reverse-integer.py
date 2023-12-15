class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        reversed_number = 0
        number = x
        negative = False
        if number < 0:
            negative = True
            number = number * (-1)
        while number != 0:
            remainder = number % 10
            reversed_number = reversed_number * 10 + remainder
            number = number // 10
        if negative:
            reversed_number = reversed_number * (-1)
        if reversed_number > INT_MAX or reversed_number < INT_MIN:
            return 0
        return reversed_number
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        arr = []
        greatest_integer = 0
        for i in range(len(digits)):
            greatest_integer += (digits[i] * (10 ** (len(digits)-i-1)))
        greatest_integer = greatest_integer + 1
        string = str(greatest_integer)
        for number in string:
            num = int(number)
            arr.append(num)
        return arr
    
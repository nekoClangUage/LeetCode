def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    bool_plusone = False
    digits_count = len(digits)
    for digit_id in range(digits_count - 1, 0, -1):
        if(digits[digit_id] < 9):
            digits[digit_id] += 1
            bool_plusone = True
            break
        else:
            digits[digit_id] = 0
    if(not bool_plusone):
        if(digits[0] < 9):
            digits[0] += 1
        else:
            digits[0] = 0
            digits.insert(0, 1)
    return digits
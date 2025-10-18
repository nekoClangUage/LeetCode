def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    sum_value = 0
    digit_capacity_a = len(a)
    digit_capacity_b = len(b)
    for pow_id in range(digit_capacity_a):
        if(a[pow_id] == '0'):
            continue
        sum_value = sum_value + pow(2, digit_capacity_a - pow_id - 1) 
            
    for pow_id in range(digit_capacity_b):
        if(b[pow_id] == '0'):
            continue
        sum_value = sum_value + pow(2, digit_capacity_b - pow_id - 1) 
    
    return bin(sum_value)[2:] 
        

addBinary(None, "101", "001")
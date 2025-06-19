

def narcissistic( value ):
    str_value = list(str(value))
    base = len(str_value)
    comp = 0
    
    for string in str_value:
        num = int(string)
        comp += num**base
    
    return comp == value
    
        
    
assert narcissistic(153) == True
assert narcissistic(1634) == True
assert narcissistic(123) == False
assert narcissistic(9474) == True
assert narcissistic(9475) == False
assert narcissistic(407) == True
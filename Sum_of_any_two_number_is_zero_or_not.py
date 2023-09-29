def add_num(l):
    """
    The function `add_num` checks if there are two numbers in a given list whose sum is zero.
    
    :param l: The parameter `l` is a list of numbers
    :return: The function `add_num` returns `True` if there are two numbers in the list `l` whose sum is
    zero, otherwise it returns `False`.
    """
    if len(l)<2:
        return False
    l1=set(l)
    for i in l:
        if -i in l1:
            return True
    
    return False
#List declared
l=[1,2,3,4,5,-1,-2,2,5,4]
#print value
print(add_num(l))
def is_panlindrome(str):
    """
    The function `is_panlindrome` checks if a given string is a palindrome or not.
    
    :param str: The parameter `str` is a string that we want to check if it is a palindrome
    :return: a boolean value indicating whether the given string is a palindrome or not.
    """
    len_str=len(str)
    c=0
    for i in range(len_str):
        if(str[i]==str[len_str-i-1]):
            continue
        else:
            c=1
            break
        
    return c==0

print(is_panlindrome('abba'))
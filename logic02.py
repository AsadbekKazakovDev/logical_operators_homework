def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is positive".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    return a>0 and b>0
a,b = 5,3
print(main(a,b))
a,b = 4,-1
print(main(a,b))
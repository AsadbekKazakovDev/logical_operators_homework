def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a>99
a=4
print(main(a))
a=33
print(main(a))
a=334
print(main(a))
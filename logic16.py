def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a>9999
a = 2839
print(main(a))
a = 97939
print(main(a))
a = 549
print(main(a))
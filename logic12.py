def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    bir = a//10
    ikki=a%10
    return bir==ikki
a = 32
print(main(a))
a = 66
print(main(a))
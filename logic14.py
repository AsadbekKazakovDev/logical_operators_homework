def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    bir = a//10
    ikki  = a%10
    summ = bir + ikki
    return summ%2==1
a = 43
print(main(a))
a = 53
print(main(a))
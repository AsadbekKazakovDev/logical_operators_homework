def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    bir  = a//10
    ikki = a%10
    summ = bir+ikki
    return summ%2==0
a = 32
print(main(a))
a = 59
print(main(a))
def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    bir  = a//100
    ikki = (a//10)%10
    uch = a%10
    summ = bir + ikki + uch
    return summ%2==1
a = 329
print(main(a))
a = 489
print(main(a))
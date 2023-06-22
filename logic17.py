def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    
    """
    bir = a//10000
    ikki = (a//1000)%10
    uch = (a//100)%10
    turt = (a//10)%10
    besh = a%10
    k = bir>ikki and ikki>uch and uch>turt and turt>besh
   
    return k 
a = 12345
print(main(a))
a = 75421
print(main(a))

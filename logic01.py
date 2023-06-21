def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    return (a>b and b>c and a>c) or (b>a and b<c and a<c)
a,b,c = 3 , 4 , 5
print(main(a,b,c))
a,b,c = 6,4,5
print(main(a,b,c))
a,b,c = 6,4,1
print(main(a,b,c))
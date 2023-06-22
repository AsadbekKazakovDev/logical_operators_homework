def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    x1=n%10
    n//=10
    x2=n%10
    n//=10
    x3=n%10
    n//=10
    x4=n%10
    n//=10
    x5=n%10

    return (n>=1000 and x1+x2+x3+x4+x5>2) or (n<1000 and x1+x2+x3+x4+x5>=2)
n = 101000
print(main(n))
n = 1101
print(main(n))
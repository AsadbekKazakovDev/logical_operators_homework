def main(x):
    """
    Given a two digit integer x, return true if x is palindrome integer.
    An integer is a palindrome, when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    uch = (a//100)%10
    turt = (a//10)%10
    besh = a%10
    return besh*100+turt*10+uch == a
a = 121
print(main(a))
a = 189
print(main(a))

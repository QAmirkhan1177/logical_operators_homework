def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x=bool(a>10 and a<99==a%111)
    return x
print(main(22))
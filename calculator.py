

def sum(a, b):
    """
    param: a, b are numeric values \n
    return: will be the Sum of them"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Only numbers are allowed")
    return a + b

def subtract (a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Only numbers are allowed")
    return a - b

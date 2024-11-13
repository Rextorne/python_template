

def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Only numbers are allowed")
    return a + b

def subtract (a, b):
    return a - b
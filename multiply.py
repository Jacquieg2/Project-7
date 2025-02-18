def multiply(a, b):
    # Base case: if b is 1, the result is just a (since a * 1 = a)
    if b == 1:
        return a
    # Recursive case: add a to the result of multiply(a, b - 1)
    return a + multiply(a, b - 1)

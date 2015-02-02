def max(l):
    """Finds the maximum in a list of numbers."""
    if len(l) == 1:
        return l[0]
    elif l[0] > max(l[1:]):
        return l[0]
    else:
        return max(l[1:])


x = [5, 2, 1, 2, 4]
print(max(x))
"""Recusive Fibonacci Sequence"""

def fib(n):
    """Returns the nth number in a Fibonacci sequence"""
    if n == 0:
        return 0
    elif n == 1: 
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__== "__main__":
    """Example"""
    print (fib(5))
    print(fib(6))
    print(fib(7))
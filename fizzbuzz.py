<<<<<<< HEAD
"""Prints results of fizz buzz form 1 to 100."""

if __name__ == "__main__":
    for x in range(1, 101):
        line = "Fizz" * (not x % 3)
        line += "Buzz" * (not x % 5)
        line += str(x) * (not line)
        print(line)
=======
"""Totes a program"""

def fizzbuzz(n):
    """Does the FizzBuzz thing n times"""
    for x in range(1, n+1):
        if x % 5 == 0 and x % 3 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)

if __name__ == "__main__":
    fizzbuzz(30)
>>>>>>> FETCH_HEAD

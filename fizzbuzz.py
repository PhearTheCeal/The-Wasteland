"""Prints results of fizz buzz form 1 to 100."""

if __name__ == "__main__":
    for x in range(1, 101):
        line = "Fizz" * (not x % 3)
        line += "Buzz" * (not x % 5)
        line += str(x) * (not line)
        print(line)

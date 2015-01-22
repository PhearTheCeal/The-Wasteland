"""Converts various currencies to other currencies."""
from sys import argv as arguments


CONVERSIONS = {"USD": 1.0,
               "FRANC": 1.2,
               "RUP": 2.0,
               "AUS": 0.3,
               "FUK": 0.5}


def check_args(args):
    """Print an error message and exit if args are bad,
    otherwise do nothing."""

    try:
        assert len(args) == 4
        assert args[1].replace('.', '', 1).isdigit()
        assert args[2] in CONVERSIONS
        assert args[3] in CONVERSIONS
    except AssertionError:
        print("Proper Usage: AMMOUNT FROM TO")
        print("Example: 34.67 USA FRANC")
        print("Kown Codes:")
        for key in CONVERSIONS:
            print(key)
        exit()


def do_conversion():
    """Take command line arguments and display conversions."""

    check_args(arguments)

    ammount = float(arguments[1])
    froom = arguments[2]
    too = arguments[3]
    res = ammount * (CONVERSIONS[froom] / CONVERSIONS[too])
    print("{:,.2f} {} = {:,.2f} {}".format(ammount, froom, res, too))

if __name__ == "__main__":
    do_conversion()

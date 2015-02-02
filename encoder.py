import string

BS64 = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"


def encode(string):
    """Takes a string and returns the Base64 representation."""

    # Get bytes of string
    str_bytes = bytes(string, "utf-8")
    return encode_bytes(str_bytes)

def encode_bytes(str_bytes):
    """Takes bytes and returns Base64 encoding."""

    # Get bytes as an int
    str_int = b_to_i(str_bytes)

    # keeping track of where we are
    num_bytes = len(str_bytes)
    chunks = num_bytes // 3
    res = ""

    # The mask to get the 6 bits we want.
    # Start it on the left end.
    bits_left = 8 * num_bytes - 6
    mask = 63 << bits_left
    for _ in range(4 * chunks):
        # convert the next 3 bytes into 4 base-64 chars
        num = (str_int & mask) >> bits_left
        res += BS64[num]
        bits_left -= 6
        mask = mask >> 6

    # get stuff we missed
    num_missed_bytes = num_bytes % 3
    if num_missed_bytes:
        missed_bytes = str_bytes[-num_missed_bytes:]
        missed_bytes += b"\x00" * (-num_bytes % 3)
        res += encode_bytes(missed_bytes)

    # handle padding
    num_padding = -num_bytes % 3
    res = res[:len(res) - num_padding] + "=" * num_padding

    return res


def b_to_i(bytes):
    """Converts bytes to an int"""
    res = 0
    for b in bytes:
        res = res << 8
        res = res | b
    return res

if __name__ == "__main__":
    print(
        "Give me a line of text, and I'll give you the Base 64 representation!")
    print("Give me a blank line (Just press enter!) to quit me.")
    while True:
        user_input = input(">>> ")
        if user_input == "":
            break
        print(encode(user_input))
        print("")
    print("Bye!")

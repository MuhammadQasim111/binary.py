def add_binary(str1, str2):
    """
    Given two binary strings str1 and str2, return their sum as a binary string.

    Args:
        str1: The first binary string.
        str2: The second binary string.

    Returns:
        The sum of str1 and str2 as a binary string.
    """
    # Use Python's built-in functions for simplicity and efficiency.
    # Convert the binary strings to integers. The base is specified as 2.
    int1 = int(str1, 2)
    int2 = int(str2, 2)
    
    # Add the two integers together.
    int_sum = int1 + int2
    
    # Convert the sum back to a binary string. The `bin()` function returns a
    # string with a '0b' prefix, so we slice it off.
    binary_sum = bin(int_sum)[2:]
    
    return binary_sum

# Example usage (uncomment to test):
# print(add_binary("11", "1"))      # Expected output: "100"
# print(add_binary("1010", "1011"))  # Expected output: "10101"
# print(add_binary("1", "0"))       # Expected output: "1"

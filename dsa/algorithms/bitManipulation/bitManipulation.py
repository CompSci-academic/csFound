# Example 1: Setting a Bit at a Specific Position
def set_bit(num, position):
    mask = 1 << position  # Create a mask with a 1 at the desired position
    return num | mask  # Set the bit at that position to 1

num1 = 5  # 101 in binary
position1 = 1  # Set the 2nd bit (0-based index)
result1 = set_bit(num1, position1)
print("Setting bit at position", position1, "in", num1, "results in", result1)

# Example 2: Clearing a Bit at a Specific Position
def clear_bit(num, position):
    mask = ~(1 << position)  # Create a mask with a 0 at the desired position
    return num & mask  # Clear the bit at that position

num2 = 6  # 110 in binary
position2 = 0  # Clear the 1st bit (0-based index)
result2 = clear_bit(num2, position2)
print("Clearing bit at position", position2, "in", num2, "results in", result2)

# Example 3: Toggling a Bit at a Specific Position
def toggle_bit(num, position):
    mask = 1 << position  # Create a mask with a 1 at the desired position
    return num ^ mask  # Toggle (invert) the bit at that position

num3 = 3  # 11 in binary
position3 = 1  # Toggle the 2nd bit (0-based index)
result3 = toggle_bit(num3, position3)
print("Toggling bit at position", position3, "in", num3, "results in", result3)

# Example 4: Checking if a Bit at a Specific Position is Set
def is_bit_set(num, position):
    mask = 1 << position  # Create a mask with a 1 at the desired position
    return (num & mask) != 0  # Check if the bit at that position is set

num4 = 10  # 1010 in binary
position4 = 2  # Check the 3rd bit (0-based index)
result4 = is_bit_set(num4, position4)
print("Is the bit at position", position4, "set in", num4, "?", result4)

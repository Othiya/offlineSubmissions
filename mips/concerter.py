def binary_to_hex(binary_str):
    # Ensure the binary string is 13 bits long
    if len(binary_str) != 13:
        raise ValueError("Input must be a 13-bit binary string")
    
    # Convert binary string to integer
    decimal = int(binary_str, 2)
    
    # Convert integer to hexadecimal
    hex_str = hex(decimal)
    
    # Return the hexadecimal string without the '0x' prefix
    return hex_str[2:].upper()

# Example usage:
binary_str = "0000000100100"  # 13-bit binary string
hex_result = binary_to_hex(binary_str)
print(f"Binary: {binary_str} -> Hex: {hex_result}")

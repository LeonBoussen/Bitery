# To convert input data to binary code
def data_to_binary(text: str) -> str:
    return ''.join(format(ord(c), '08b') for c in text)

# To convert binary to a string
def binary_to_data(binary: str) -> str:
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

#remove the the last 0 character to make sure to not have large empty spaces
def clean_binary(binary):
    return binary.rstrip('0' * 8)  # removes trailing null characters


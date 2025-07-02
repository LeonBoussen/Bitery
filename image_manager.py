from PIL import Image
import math

#def binary_to_image(binary_string: str, width: int = 1080, height: int = 1080, output_path: str = "output.jpg"):
#
#    # Ensure the binary string has exactly width * height bits
#    expected_length = width * height
#    if len(binary_string) < expected_length:
#        binary_string = binary_string.ljust(expected_length, '0')
#    elif len(binary_string) > expected_length:
#        binary_string = binary_string[:expected_length]
#
#    # Create a new black and white (mode '1') image
#    img = Image.new('1', (width, height))  # Mode '1' = 1-bit pixels, black and white
#
#    # Convert the binary string to pixel values (0 or 1)
#    pixels = [int(bit) for bit in binary_string]
#
#    # Put data into the image
#    img.putdata(pixels)
#
#    # Save the image
#    img.save(output_path)
#    print(f"Image saved to {output_path}")
#    return output_path


def binary_to_image(binary_string: str, output_path: str = "output.jpg") -> str:
    """
    Converts a binary string (e.g. '010101...') to a grayscale image 
    where white = 1, black = 0. The image is just large enough to fit all data.
    """
    try:
        # Calculate required number of pixels
        num_bits = len(binary_string)
        side_length = math.ceil(math.sqrt(num_bits))  # Make square image
        total_pixels = side_length * side_length

        # Pad binary string to match pixel count
        padded_binary = binary_string.ljust(total_pixels, '0')

        # Create pixel data (1 = white, 0 = black)
        pixels = [(255 if bit == '1' else 0) for bit in padded_binary]

        # Create image
        img = Image.new("L", (side_length, side_length))  # "L" mode = grayscale
        img.putdata(pixels)
        img.save(output_path)

        print(f"[+] Image saved to: {output_path} ({side_length}x{side_length})")
        return output_path

    except Exception as e:
        print(f"[!] Failed to convert binary to image: {e}")
        return None

def image_to_binary(image_path: str) -> str:

    img = Image.open(image_path).convert('1')  # Ensure image is in 1-bit mode
    width, height = img.size
    pixels = img.load()

    binary_string = ''
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            binary_string += '1' if pixel == 255 else '0'
    
    return binary_string
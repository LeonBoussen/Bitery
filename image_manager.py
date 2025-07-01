from PIL import Image

def binary_to_image(binary_string: str, width: int = 1080, height: int = 1080, output_path: str = "output.png"):

    # Ensure the binary string has exactly width * height bits
    expected_length = width * height
    if len(binary_string) < expected_length:
        binary_string = binary_string.ljust(expected_length, '0')
    elif len(binary_string) > expected_length:
        binary_string = binary_string[:expected_length]

    # Create a new black and white (mode '1') image
    img = Image.new('1', (width, height))  # Mode '1' = 1-bit pixels, black and white

    # Convert the binary string to pixel values (0 or 1)
    pixels = [int(bit) for bit in binary_string]

    # Put data into the image
    img.putdata(pixels)

    # Save the image
    img.save(output_path)
    print(f"Image saved to {output_path}")


def read_binary_from_image(image_path: str) -> str:

    img = Image.open(image_path).convert('1')  # Ensure image is in 1-bit mode
    width, height = img.size
    pixels = img.load()

    binary_string = ''
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            binary_string += '1' if pixel == 255 else '0'
    
    return binary_string
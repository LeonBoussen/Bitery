import binary_manager as bitman
import image_manager as imgman
import os

#note only text works but that is prob because the utf-8 encoding method


def main_menu():
    try:
        user_input = int(input("1. Make image\n2. Read image\n3. Execute image\n4. reasable file from image\nchoice: "))
        if user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4:
            print("Wrong input")
        
        elif user_input == 1:
            make_img()

        elif user_input == 2:
            print(read_img())

        elif user_input == 3:
            execute_image()
        
        elif user_input == 4:
            reasemble_file_from_image()

    except Exception as e:
        print(f"error: {e}")
        input("Press Enter to continue")

# Function to convert data to binary and then create the image
def make_img():
    choice = int(input("1. Text message\n2. File\nChoice: "))

    if choice == 1:
        data = input("Enter your message: ")
    elif choice == 2:
        file_path = input("Path to your file: ")
        if not os.path.isfile(file_path):
            print("This is not a file!")
            return
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                data = f.read()
        except Exception as e:
            print(f"Failed to read file: {e}")
            return
        
    binary = bitman.data_to_binary(data)
    img = imgman.binary_to_image(binary)
    os.system(f"start {img}")


# Function to read the binary from the image
def read_img():
    img_path = input("Enter path to image\nPath: ")
    if img_path == "":
        img_path = "output.jpg"

    binary = imgman.image_to_binary(img_path)
    clean_binary = bitman.clean_binary(binary)
    data = bitman.binary_to_data(clean_binary)
    return data

def execute_image():
    code = read_img()
    exec(code, globals())

def reasemble_file_from_image(img_path=None, output_filename=None):
    """
    Reads an image with embedded binary data (e.g., exe, image, txt), 
    decodes it, and writes it as a binary file to disk.
    """
    if not img_path:
        img_path = input("Enter path to image\nPath: ").strip()
        if not img_path:
            img_path = "output.jpg"

    try:
        # Step 1: Read binary from image
        binary_string = imgman.image_to_binary(img_path)

        # Step 2: Clean the binary string
        clean_binary = bitman.clean_binary(binary_string)

        # Step 3: Convert binary string to bytes
        byte_data = int(clean_binary, 2).to_bytes((len(clean_binary) + 7) // 8, byteorder='big')

        # Step 4: Choose filename
        if not output_filename:
            output_filename = input("Save as file (include extension): ").strip()
            if not output_filename:
                output_filename = "output.bin"

        # Step 5: Write to binary file
        with open(output_filename, 'wb') as f:
            f.write(byte_data)

        print(f"[+] File saved as: {output_filename}")
        return output_filename

    except Exception as e:
        print(f"[!] Failed to extract file from image: {e}")
        return None

if __name__== "__main__":
    while True:
        main_menu()
import binary_manager as bm
import image_manager as im

def main_menu():
    try:
        user_input = int(input("1. make image\n2. read image\nchoice: "))
        if user_input != 1 and user_input != 2:
            print("Wrong input")
        
        elif user_input == 1:
            make_img()

        elif user_input == 2:
            read_img()

    except Exception as e:
        print(f"error: {e}")
        input("Press Enter to continue")

def make_img():
    print("Hallo")

    
def read_img():
    print("Hallo")

if __name__== "__main__":
    while True:
        main_menu()
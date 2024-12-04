MINIMUM_HEIGHT = 50

def main():
    """
    Checks if the user meets the minimum height requirement to ride.
    Continuously prompts the user until no input is provided.
    """
    while True:
        height_input = input("How tall are you? (Press Enter to exit) ")
        if not height_input:  
            print("Thank you for checking. Goodbye!")
            break
        
        try:
            height = float(height_input)  
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number for your height.")

if __name__ == '__main__':
    main()
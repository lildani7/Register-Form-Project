import emoji
import random

def register_user():

    print("\nRegistering...")
    
    age = get_valid_age()
    user_code = int(random.randint(1_000_000, 10_000_000) / age)

    print("\n\nRegistering was successful!")
    print(f"Your user code = {user_code}\n\n") 
    print(emoji.emojize("Your register proccess has been finished!\nHave a good day! :red_heart:", variant="emoji_type"))


def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            temp = 1 / age

            if age < 0:
                raise ValueError("Age can not be negative!")
                
            if age < 18:
                raise PermissionError("You can not access this content due to your age..")
                
        except ValueError as e:
            print(f"\nError: {e}\n\n")
        
        except PermissionError as e:
            print(f"\nError: {e}\n\n")
        
        except ZeroDivisionError:
            print("\nAge can not be zero!\n\n")

        except Exception as e:
            print(f"\nError: {e}\n\n")

        else:
            return age

def create_new_file():
    ''' In this code, 'good_record.txt' is the name of the file to be opened. The 'r' argument means the file is opened in read mode.
   The as f part assigns the opened file to the variable f. Then, f.read() is used to read the entire content of the file, which is stored in the  '''
    with open('Names_Entered.txt' , 'r' ) as f:
        #This prints the content of the file
        print(f.read())
# A class creates a template for objects that dont exist in premade form for python.
# This Class creats an exception that does not exist in pyhton
class LengthError(Exception):
    #Pass teel tell the code to go the next line
    pass
# This Class creats an exception that does not exist in pyhton
class SpecialCharacterError(Exception):
    #Pass teel tell the code to go the next line
    pass
# A definition or DEF creates a function for pyton to use later.
# This def creates 2 functions one to check for length errors and the other for special character errors 
def check_input(input_string):
    # The special character should not be in names
    special_characters = "~!@#$%^&*()_+=-`:\"';/[/[/}/{:;\"'</,>.|\\"
    # The max legth prevents overrun in name length
    max_length = 50  # Define a maximum length for the names
    # This line of code checks if the length of 'input_string' exceeds 'max_length'.
    # If the length of 'input_string' is greater than 'max_length', the condition becomes True.
    if len(input_string) > max_length:
        # The 'raise' keyword is used to throw an exception if a condition occurs. In this case, LengthError is raised when the input exceeds the maximum allowed length.
        raise LengthError(f"Input is too long. Maximum length is {max_length} characters.")
    # The 'for' Keyword is used to itterate in the input string from the user. 
    for character in input_string:
        #This if is only triggered in the event of special character being used in entry thats not allowed.
        if character in special_characters:
            # This raise condition is activated int event of invalid charter being tyoed in a name
            raise SpecialCharacterError(f"Special character '{character}' is not allowed.")
def main():
    while True: 
        User_input = input('Would you like to record your name and email (Yes or NO)?')
        if User_input.lower() == 'yes':
            try:
                # This tells the user what to enter and how to enter numbers
                user_input_line1 = input('Write your first name here (use Roman numerals to indicate numbers): ')
                # This calls the definition earlier created to verify which special characters are not allowed. 
                # Also checks to see if the maximum character limit is reached
                check_input(user_input_line1)
                # This tells the user what they entered
                print('Your First Name is:', user_input_line1)
            except SpecialCharacterError as e:
                print(e, 'You have entered an invalid Character')
                continue

            try:
                # This initiates user input to be used in the if statement 
                user_input_line2 = ('')
                # Asks the user if they have a middle name
                user_answer2 = input('Do you have a middle name? (Yes or NO)')
                # Checks the input from the user
                check_input(user_answer2)
                # If the user answers 'yes', it asks for the middle name
                if user_answer2.lower() == 'yes':
                    # Prints this to user 
                    user_input_line2 = input('Enter middle name here: ')
                    # Checks the user input
                    check_input(user_input_line2)
                    print('Your middle name is:', user_input_line2)
                # If the user answers 'no', it prints 'Go to next line'
                elif user_answer2.lower() == 'no':
                    print('Go to next line')
            except SpecialCharacterError as e:
                print(e, 'You have entered an invalid record')
                continue

            try:
                # Asks the user to input their last name
                user_input_line3 = input('Write your last name here: (use Roman numerals to indicate numbers):')
                # Checks the input from the user
                check_input(user_input_line3)
                # Print the user input from input_line3
                print(' Your Last name is:' ,user_input_line3)
            except SpecialCharacterError as e:
                print(e, 'You have entered an invalid record')
                continue

            # Asks the user to input their email
            user_input_line4 = input('Write your email here: ')
            # Prints the user's first name, middle name (if any), last name, and email
            print('Your name is:' , user_input_line1 , user_input_line2 , user_input_line3,'Your Email is:' , user_input_line4)
            # Opens the file 'good_record.txt' in append mode
            with open('Names_Entered.txt', 'a') as f:
                # Writes the user's first name, middle name (if any), last name, and email to the file
                f.write(f'{user_input_line1} {user_input_line2} {user_input_line3} {user_input_line4}\n')
            # Calls the function 'create_new_file()' 
            create_new_file()
        elif User_input.lower() == 'no':
            break
        else:
            print("Invalid input. Please enter either 'Yes' or 'No'.")
 # If this script is run directly (instead of being imported), it calls the function 'main()'   
if __name__ == "__main__":
    main()
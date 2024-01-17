# The 'import' statement in Python allows us to use code from other modules.
# A module is a file containing Python definitions and statements.
# When 'import Names' is used, it means we are importing the 'Names' module.
# After importing, we can use any functions, classes, or variables defined in the 'Names' module by referencing them as 'Names.<name>
# The 'Names' module allows the user to record their name into a file that can be Serched 
import Names
# The 'Search' module allows the user to perform a a serch in a text file
import Search
#Def Main defines the main fuction
def main():
    # The while true loop allows the program to continously run until a condtion is met to end the program 
    while True:
        #This allows the user to know what to do in the to get back to the main function
        print('Note in the search function you must selct "No" To exit the "Search" program ')
        # The 'try' statement is used for exception handling in Python. 
        # It allows us to write code that might raise an exception in a 'try' block.
        # If an exception occurs, the code in the 'try' block stops executing, and the code in the 'except' block runs.
        # If no exception occurs, the 'except' block is skipped. 
        try: 
            # THe user_input function tell s the user what the menu options are
            user_input = int(input('Selcet to 1 enter Your Name,/ Select 2 to enter the search functio,/ and Select 3 to exit: '))
            #The if tells python what to do if the statemnet is true 
            if user_input == 1: #This option calls the functions in 'Names' main function if the user inputs is 1
                Names.main()
            elif user_input == 2: #This option calls the functions in 'Serch' main function if the user inputs is 2
                Search.main()
            elif user_input ==3: #This option ends the program if option 3 is selectex
                #This is  only printed if the option 3 is chosen 
                print('Thank you for using my Program')
                # Break in Python breaks the loop and end the program 
                break
        #This checks to see if the is a numerical error in the user input     
        except ValueError:
            #This mesage is only printed if (1, 2, or 3) is not enter in the user input 
            print('Only Enter 1,/ 2,/ 3')        
       
  # If this script is run directly (instead of being imported), it calls the function 'main()'   
if __name__ == "__main__":
    main()   
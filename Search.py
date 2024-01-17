def user_search(file_name, keyword):
    # Initialize a flag to track if any results were found
    found = False 
    # Open the file in read mode
    with open(file_name) as file:
         # Iterate over each line in the file, with line numbers starting at 1.
        for line_number, line in enumerate(file, start=1):
            # Check if the keyword is in the current line.
            if keyword in line:
                # If the keyword is found, print the line number and the line (stripped of leading/trailing whitespace).
                print(f'Keyword "{keyword}" found at line {line_number}: {line.strip()}')
                # Set the flag to True if a result is found
                found = True 
                    # If no results were found (i.e., if the flag is still False), print a message indicating no results.           
    if not found:
        #This prints a this messag if no results are found
        print('Sorry, no results found')
#Def Main defines the main fuction of the program       
def main():
    ## The while true loop allows the program to continously run until a condtion is met to end the program
    while True:
        # Prints to the user what to do
        user_answer = input('Would like to conduct a search Yes or No: ' )
        # Check if the answer ius yes or no
        while user_answer.lower() not in ['yes', 'no']:
            if user_answer == '':
                print('You hit enter without typing anything. Please enter either "Yes" or "No".')
            # prints if the inoput as invalid
            print('Invalid input. Please enter either "Yes" or "No".')
        # This if Luanches the seaarch function        
        if user_answer.lower() == 'yes':
            # Tells The user to enter the keyword the want to search for
            keyword = input('Enter the keyword to search for: ')
            # Prints the results of the search 
            user_search('Names_Entered.txt', keyword)
            # If the user answers 'no', it prints Thank you for using my program
        elif user_answer.lower() == 'no':
            print('Thank you for using my Program')
            #Stops the Loop
            break
  # If this script is run directly (instead of being imported), it calls the function 'main()'   
if __name__ == "__main__":
    main()

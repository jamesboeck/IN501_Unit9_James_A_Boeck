import Names
import Search

def main():
    while True:  
        try: 
            print('Mote you must enter no aat the end of the program to go to the next function')
            user_input = int(input('Select 1 to enter Your Name, Select 2 to enter the search function, and Select 3 to exit: '))
            if user_input == 1:
                Names.main()
            elif user_input == 2:
                Search.main()
            elif user_input == 3:
                print('Thank you for using my Program')
                break
        except ValueError:
            print('Only Enter 1, 2, or 3')        

if __name__ == "__main__":
    main()

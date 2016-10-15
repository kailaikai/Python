#Importing the modules needed to run some methods.
import sys
import os
import csv


#The list is empty by default - it's up to the user to add values to it.
List1 = []


#This class deals with everything related to the main function of the program.
class main:
    def showlist(): #Shows all the values present in the list. It is first empty.
        if not List1:
            print("The list is empty!")
        else:
            for Item in List1:
                print(Item,end=" ")
    def removevalue(): #Removes a user-defined entry from the list.
        aux.clearwindow()
        try:
            entry = "%g" % float(input("Type in the entry to be removed: "))
        except(NameError,ValueError):
            print("That is not a valid input.")
            os.system("pause")
            aux.clearwindow()
            main.menu()
        except(KeyboardInterrupt):
            print("KeyboardInterrupt Error. Exiting program...")
            os.system("pause")
            sys.exit(1)
        except(EOFError):
            print("EOFError. Exiting program...")
            os.system("pause")
            sys.exit(1)
        if entry in List1:
            List1.remove(entry)
            print("The entry was successfully removed!")
            aux.input_wait()
            main.menu()
        else:
            print("There's no such item in the list.")
            input("Press ENTER to return to the main command line.")
            aux.clearwindow()
            main.menu()
    def addvalue(): #Adds a user-defined entry to the list.
        aux.clearwindow()
        try:
            entry = "%g" % float(input("Type in the new entry: "))
        except(NameError,ValueError):
            print("That is not a valid input.")
            os.system("pause")
            aux.clearwindow()
            main.menu()
        except(KeyboardInterrupt):
            print("KeyboardInterrupt Error. Exiting program...")
            os.system("pause")
            sys.exit(1)
        except(EOFError):
            print("EOFError. Exiting program...")
            os.system("pause")
            sys.exit(1)
        if (float(entry) >= 0) and (float(entry) <= 20):
            List1.append(entry)
            print("The new entry was successfully added!")
            aux.save_data("ListManagerEntries.csv", entry)
            aux.input_wait()
            main.menu()
        else:
            print("That is not a valid input. Try again.")
            print("Press ENTER to return to the main command line.")
            aux.clearwindow()
            main.menu()
    def menu(): #Main menu, through where the user navigates the program methods.
        aux.clearwindow()
        try:
            Option = (input("Type 'help' \
for a list of commands.\n> "))
            OptionLowercase = str.lower(Option)
        except(NameError,ValueError): #Unexpected inputs.
            print("That is not a valid input.")
            os.system("pause")
            aux.clearwindow()
            main.menu() 
        except(KeyboardInterrupt): #Ctrl-C.
            print("KeyboardInterrupt Error. Exiting program...")
            os.system("pause")
            sys.exit(1) 
        except(EOFError): #Read beyond file.
            print("EOFError. Exiting program...")
            os.system("pause")
            sys.exit(1) 
        if OptionLowercase in ['list']:
            aux.clearwindow()
            main.showlist()
            aux.input_wait()
            main.menu()
        elif OptionLowercase in ['exit','quit']:
            os.system("pause")
            sys.exit(1)
        elif OptionLowercase in ['help']:
            aux.clearwindow()
            print("\
> 'help': Shows a list of available commands.\n\
> 'list': Displays the saved list.\n\
> 'add': To add a new value to the list.\n\
> 'remove': To remove a value from the list.\n\
> 'quit': Quits the program.\n")
            aux.input_wait()
            aux.clearwindow()
            main.menu()
        elif OptionLowercase in ['add']:
            aux.clearwindow()
            main.addvalue()
        elif OptionLowercase in ['remove']:
            aux.clearwindow()
            main.removevalue()
        else:
            if Option == "":
                print("Please input a value.")
                os.system("pause")
                aux.clearwindow()
                main.menu() #If there's no input by the user.
            else:
                print("That is not a valid input.")
                os.system("pause")
                aux.clearwindow()
                main.menu()


#This class is used as an auxiliary to the main class, by housing methods that are auxiliary
#to the main class.
class aux:
    def clearwindow(): #Clears the window.
        clear = lambda: os.system('cls')
        clear()
    def input_wait(): #Awaits for any user input.
        input_wait = input("\nPress ENTER to return \
to the main command line.")
    def save_data(Filename = "", List1 = []): #Saves user entries.
        with open(Filename,
                  "w", newline='\n') as csvfile:
            DataWriter = csv.writer(
                csvfile,
                delimiter='\n',
                quotechar=" ",
                quoting=csv.QUOTE_NONNUMERIC)
            DataWriter.writerow(List1)
            csvfile.close()
            print("Data saved!")
    def read_data(Filename = ""): #Reads previously submitted used input.
        with open(Filename,
                  "r", newline='\n') as csvfile:
            DataReader = csv.reader(
                csvfile,
                delimiter="\n",
                quotechar=" ",
                quoting=csv.QUOTE_NONNUMERIC)

            Output = []
            for Item in DataReader:
                Output.append(List1)

            csvfile.close()


#The program is initiated here by calling the menu method of the main class.
main.menu()
aux.read_data("ListManagerEntries.csv")

# This program is protected by a CC BY-SA 4.0 License.
# To know more, go to https://creativecommons.org/licenses/by-sa/4.0/legalcode
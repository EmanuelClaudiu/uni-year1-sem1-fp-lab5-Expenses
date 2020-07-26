from verification.inputValidation import *
import time
from get_set.get import *
from services import *

class UI:

    def printMenu():
        string = ''
        string += '\n 1 - Add expense\n'
        string += '\n 2 - Display the list of expenses\n'
        string += '\n 3 - Filter the list so that it contains only expenses above a certain value\n'
        string += '\n 4 - Undo\n'
        print(string)

    def mainMenu(self):
        flag = True
        Expense = Services()
        Expense.createStartList()
        while flag:
            UI.printMenu()
            command = input("Enter command: ").strip()
            if not isInt(command):
                print("\nInvalid Command\n")
                time.sleep(1)
                print("\nPlease re-enter a valid command:\n")
                time.sleep(1)
            else:
                if command == "1":
                    userInput = input("Write expense: ").strip()
                    inputList = userInput.split()
                    inputList = validateNewExpense(inputList)
                    Expense.addExpense(getDay(inputList), getAmount(inputList), getType(inputList))
                    print("\nExpense Added\n")
                    time.sleep(1.5)
                if command == "2":
                    Expense.showAllExpenses()
                if command == "3":
                    userInput = input("The value: ")
                    Expense.filterExpenses(userInput)
                    print("\nList Filtered\n")
                    time.sleep(1.5)
                if command == "4":
                    Expense.Undo()

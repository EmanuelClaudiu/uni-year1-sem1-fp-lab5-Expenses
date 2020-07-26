from get_set.get import *
from functions.functionMods import *
import copy
import time

class Services:

    def __init__(self):
        self.data = []
        self.dataRepo = []
    
    def createStartList(self):
        self.data.append(['30', '100', 'water'])
        self.data.append(['21', '200', 'heating'])
        self.data.append(['11', '1', 'electricity'])
        self.data.append(['10', '0', 'gas'])
        self.data.append(['14', '24', 'gas'])
        self.data.append(['15', '20', 'other'])
        self.data.append(['1', '50', 'water'])
        self.data.append(['2', '1000', 'heating'])
        self.data.append(['31', '244', 'water'])
        self.data.append(['6', '211', 'electricity'])
        self.dataRepo.append(self.data)

    def addExpense(self, expenseDay, expenseAmount, expenseType):
        '''
        in order to make the undo operation possible, this function creates a new list object and does the modifications on it
        newData - list, the newly created list of expenses on which we do the new modifications
        myList - list, the list of data about an expense, which we will append to the 'newData' list
        dataRepo - list, the list containing all expenses lists thorought the changes
        data - list, the list of expenses after the last modification
        '''
        newData = []
        newData = copy.deepcopy(self.data)
        myList = [expenseDay, expenseAmount, expenseType]
        newData.append(myList)
        self.dataRepo.append(newData)
        self.data = self.dataRepo[-1]

    '''
    def testAddExpense(self):
        testRepo = copy.deepcopy(self.dataRepo)
        try:
            Services.addExpense('1','20','water')
            assert (getAmount(self.dataRepo[-1]) == 20)
            Services.addExpense('20','30','makai')
            assert (getAmount(self.dataRepo[-1]) == 'makai')
        except:
            pass

    Services.testAddExpense()
    '''
    
    def showAllExpenses(self):
        '''
        the function parses all objects of the class list, and it prints the expenses using an index
        '''
        i = 0
        for x in self.data:
            print (str(i) + '.' , 'Day:' + str(getDay(x)), ';' , 'Amount:' + str(getAmount(x)) , ';' , 'Type:' + str(getType(x)))
            i += 1
        time.sleep(1.5)
    
    def filterExpenses(self, value):
        newData = []
        for x in self.data:
            if int(getAmount(x)) > int(value):
                newData.append(x)
        self.dataRepo.append(newData)
        self.data = self.dataRepo[-1]

    def Undo(self):
        if not self.dataRepo:
            print("\nThe expense list is empty... could not perform Undo\n")
            time.sleep(1.5)
        else:
            del self.dataRepo[-1]
            if not self.dataRepo:
                self.data = []
            else:
                self.data = self.dataRepo[-1]
            print("\nUndo operation successful\n")
            time.sleep(1.5)
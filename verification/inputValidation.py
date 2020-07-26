import time

def isInt(myString):
    '''
    validates a command entered in the starting menu
    '''
    if myString == '1' or myString == '2' or myString == '3' or myString == '4':
        return True
    else:
        return False

def validateNewExpense(newExpense):
    while True:
        ok = 0
        errorString = ''
        try:
            a = int(newExpense[0])
            if a<0 or a>31:
                errorString += '\nPlease introduce a valid day'
                ok = 1
        except:
            errorString += '\nPlease introduce a valid day'
            ok = 1
        try:
            a = int(newExpense[1])
            if a<0:
                errorString += '\nPlease introduce a valid amount'
                ok = 1
        except:
            errorString += '\nPlease introduce a valid amount'
            ok = 1
        try:
            a = str(newExpense[2])
            a = int(a)
            errorString += '\nPlease introduce a valid type'
            ok = 1
        except:
            pass
        if ok == 0:
            return newExpense
        else:
            print(errorString)
            time.sleep(1)
            userInput = input("Re-introduce the expense: ").strip()
            newExpense = userInput.split()
def getInput():
    return input("Введите строку: ")

def testInput(x):
    try:
        int(x)
        return True
    except:
        return False

def strToInt(x):
    return int(x)

def printInt(x):
    print(x)

x = getInput()
if testInput(x):
    printInt(strToInt(x))
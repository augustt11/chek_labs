def test():
    x = int(input("Enter a number: "))
    if x >= 0:
        print(positive(x))
    else:
        print(negative(x))

def positive(x):
    return 'Положительное'

def negative(x):
    return 'Отрицательное'

test()

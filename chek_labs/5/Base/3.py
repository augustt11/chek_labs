num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')

def Check(x):
    if (x.isdigit()):
        return int(x)
    else:
        new_num = ''
        for i in x:
            if i in '123457890':
                new_num += i
    if not new_num:
        return Check(input('Введите число заного: '))
    return int(new_num)
print(Check(num1) + Check(num2))

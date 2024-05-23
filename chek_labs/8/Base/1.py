class First:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def write_num(self):
        print(f'Первое число: {self.num1}, второе число: {self.num2}')
    def redact(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def Summa(self):
        return self.num1 + self.num2
    def MaxNumber(self):
        if self.num1 == self.num2:
            return '='
        elif self.num1 > self.num2:
            return '>'
        else:
            return '<'

Object = First(int(input('Введите первое число: ')), int(input('Введите второе число: ')))
Object.write_num()
print(f'{Object.num1} + {Object.num2} = {Object.Summa()}')
print(f'{Object.num1} {Object.MaxNumber()} {Object.num2}')
Operation = input('Вы хотите изменить числа? (Yes/No): ')

while Operation == 'Yes':
    Object.redact(int(input('Введите первое изменённое число: ')), int(input('Введите второе изменённое число: ')))
    Object.write_num()
    print(f'{Object.num1} + {Object.num2} = {Object.Summa()}')
    print(f'{Object.num1} {Object.MaxNumber()} {Object.num2}')
    Operation = input('Вы хотите изменить числа? (Yes/No): ')

print("Задание Base. Счастливое число")
num = input()
num = '0'*(4 - len(num)) + num
if num[:2] == num[:1:-1]:
    print('Base')
else:
    print('0')
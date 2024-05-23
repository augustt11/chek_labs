num = input("Enter a number: ")
while len(num) > 1:
    x = 0
    for i in num:
        x += int(i)
        num = str(x)
print(num)
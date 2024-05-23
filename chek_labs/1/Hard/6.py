num = int(input("Enter a number: "))
maximum = num
while num:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        break
    if num > maximum:
        maximum = num
print(maximum)
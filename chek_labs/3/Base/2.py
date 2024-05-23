def istina(x):
    return (abs(x) + 5 > 3)
def neIstina(x):
    return (abs(x) + 5 < 3)

num = int(input("Enter a number: "))

print(istina(num))
print(neIstina(num))
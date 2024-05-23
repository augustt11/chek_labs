def fibonachi(n):
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    return b

def formulaFib(n):
    sqrt_5 = 5 ** 0.5
    return ((((1 + sqrt_5) / 2) ** n - ((1 - sqrt_5) / 2) ** n) / sqrt_5)

i = 0
while True:
    i += 1
    if abs(formulaFib(i) - fibonachi(i)) > 0.001:
        print('Отличие более чем на 0.001 начинается с n =', i)
        print('При этом отличие составляет:', formulaFib(i) - fibonachi(i))
        break


num = int(input('Enter a number: '))

if 4<num%100<21 or num%10 == 0 or 4<num%10<10:
    print(f'На лугу пасётся {num} коров')
else:
    if num%10 == 1:
        print(f'На лугу пасётся {num} корова')
    if 1<num%10<5:
        print(f'На лугу пасётся {num} коровы')
def check_multiplication_knowledge():
    count_true = 0
    count_false = 0
    combo_true = 0
    combo_false = 0

    while count_true < 5:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        correct_answer = num1 * num2
        user_answer = int(input(f"Результат умножения {num1} на {num2}: "))

        if user_answer == correct_answer:
            print("Правильно!\n")
            count_true += 1
            combo_true += 1
            combo_false = 0
        else:
            print("Неправильно!")
            print(f"Правильный ответ: {correct_answer}\n")
            count_false += 1
            combo_false += 1
            consecutive_correct = 0

        if combo_true == 3 and user_answer == correct_answer:
            print("Отлично! Осталось немного!\n")
        elif combo_false == 3 and user_answer != correct_answer:
            print("Что-ж... Это весьма печально...\n")

    print('Получено 5 верных ответов, программа завершена')


# Запуск программы
check_multiplication_knowledge()
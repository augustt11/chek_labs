'''
Создайте структуру с именем train, содержащую поля: название пунктов отправления и назначения,
время отправления и прибытия. Перегрузить операцию сложения - два поезда можно сложить,
если пунк назначения первого совпадает с пунктом отправления второго и время прибытия первого раньше чем отправление второго.'''
class train:
    def __init__(self, departure, purpose, departure_time, purpose_time):
        self.departure = departure # Пункт отправления
        self.purpose = purpose # Пункт назначение
        self.departure_time = departure_time # Время отправления
        self.purpose_time = purpose_time # Время прибытия
    def __add__(self, other):
        # Проверяем условия для сложения
        if self.purpose == other.departure and self.purpose_time < other.departure_time:
            # Создаем новый поезд, объединяя информацию обоих поездов
            new_departure = self.departure
            new_purpose = other.purpose
            new_departure_time = self.departure_time
            new_purpose_time = other.purpose_time
            return train(new_departure, new_purpose, new_departure_time, new_purpose_time)
        else:
            # Если условия не выполняются, возвращаем None
            return None
train1 = train("Москва", "Санкт-Петербург", "10:00", "14:00")
train2 = train("Санкт-Петербург", "Москва", "15:00", "19:00")

combined_train = train1 + train2
if combined_train:
    print(f'Поезда ({train1.departure} - {train1.purpose}) могут быть объеденены')
else:
    print("Поезда не могут быть объединены.")
# Написать функцию shift_time, которая принимает 2 параметра: количество дней и количество секунд
# и сдвигает дату и время 01.01.2023 12:30:00 на указанное количество дней и секунд. В качестве
# выходного значения нужно вывести кортеж: день и секунда от сдвинутого времени.

# Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

import datetime

days, seconds = int(input()), int(input())

def shift_time(days: int = 0, seconds: int = 0):
    date = datetime.datetime(2023, 1, 1, 12, 30, 0) + datetime.timedelta(days=days, seconds=seconds)
    return (date.day, date.second)

print(shift_time(days, seconds))

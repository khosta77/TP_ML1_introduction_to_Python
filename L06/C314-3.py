# Написать функцию parse_time, которая принимает строку в качестве параметра, которая является временем
# формата “ГГГГ ММ ДД ЧЧ ММ СС” и парсит эту строку в объект datetime.datetime и сдвигает ее на
# один день вперед. 

# Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

import datetime

string_datetime = input()

def parse_time(s):
    date = datetime.datetime.strptime(s, "%Y %m %d %H %M %S") + datetime.timedelta(days=1)
    return date.day

print(parse_time(string_datetime))

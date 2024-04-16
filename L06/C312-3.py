# Написать функцию changed_div, которая считает отношение делителя к частному.
# Желательно, чтобы случай с нулевым делимым должен быть обработан с помощью try-except:
# при ошибке ZeroDivisionError должен возвращать делимое.

#Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

numerator, denominator = int(input()), int(input())

def changed_div(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return numerator

print(changed_div(numerator, denominator))

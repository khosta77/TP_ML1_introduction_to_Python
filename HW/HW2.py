# Необходимо написать генераторную функцию solution, которая будет фильтровать данные
# из последовательности data функцией func_filter, к полученным данным применять
# функцию func_map и возвращать в качестве значения каждый второй элемент полученной
# последовательности. Нужно пользоваться здесь концепцией генератора, то есть обрабатывать
# не все данные разом, а только те, что необходимы для возвращения следующего значения.
#Дополните также код своей реализацией кэшируещего декоратора из ДЗ 4:

def cache_deco(func):
    '''
    Взял из С39-2
    '''
    cache = {}

    def wrapper(args):
        if args not in cache:
            result = func(args)
            cache[args] = result
        return cache[args]

    return wrapper

def solution(func_map, func_filter, data):
    filtered_data = filter(func_filter, data)
    mapped_data = map(func_map, filtered_data)
    is_odd = False
    for i in mapped_data:
        if not is_odd:
            yield i
        is_odd = not is_odd
'''
def calc():
    count = 0
    @cache_deco
    def calc_(x):
        nonlocal count
        count += 1
        print("Call:", count)
        return x
    return calc_

for i in solution(calc(), lambda x: x % 2 == 1, (1, 1, 2, 2, 2, 3, 1, 2, 3, 1)):
    print(i)
'''
code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)

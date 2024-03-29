# Напишите декоратор, который будет кэшировать вызовы функции, которая будет передана на вход.
# То есть декоратор должен проверить нет ли в кэше (например, словаре) значения, и если нет,
# то вычислить и запомнить результат, если есть, то взять это значение. Дополните код ниже,
# дописав свой код в секции “YOUR CODE HERE”.

def cache_deco(func):
    cache = {}

    def wrapper(args):
        if args not in cache:
            result = func(args)
            cache[args] = result
        return cache[args]

    return wrapper

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

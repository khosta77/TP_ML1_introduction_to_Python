# В этом задании нужно будет написать свою реализацию filter()
# (https://docs.python.org/3/library/functions.html#filter), то есть генераторную функцию,
# которая принимает функцию и последовательность и фильтрует последовательность в зависимости
# от вердикта переданной функции. Воспользуйтесь своей реализацией, чтобы применить лямбда функцию,
# поданную на вход, к поданной на вход последовательности.
# Вам нужно написать свой код в секции “YOUR CODE HERE”, остальной код можно оставить как есть: 

def filter(func, seq):
    for i in seq:
        if func(i):
            yield i

func_in, seq_in = eval(input()), eval(input())

for x in filter(func_in, seq_in):
   print(x)

# Необходимо написать программу, которая будет считывать со стандартного ввода строку. 
# Нужно разбить строку на слова, словом будем считать последовательность символов 
# отличных от пробелов (то есть знаки пунктуации будут входить в слова). Далее нужно
# посчитать и вывести среднее число символов в словах этого текста. Точность проверяется
#до 2го знака после запятой (точность +-0.01). * Решение можно реализовать в 2 строки кода.
size = [len(w) for w in (input().split())]
print(round((sum(size) / len(size)), 2))

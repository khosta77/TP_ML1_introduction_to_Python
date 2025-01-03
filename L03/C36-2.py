# Необходимо написать программу, которая будет считывать со
# входа данные последовательностей чисел, считать и выводить
# их среднее значение. Напишите сначала функцию, которая будет
# принимать строку, а в ответ возвращать среднее значение чисел
# из нее. А далее применяйте эту функцию к каждой считанной
# входной последовательности. На вход будут подаваться строки,
# в которых расположены целые числа, разделенные пробелом.
# Передача пустой строки будет означать конец входных данных.
def myMean(str):
    return round((sum(str)/len(str)), 2)

while str := [int(i) for i in input().split()]:
    print(myMean(str))

# Необходимо написать программу, которая будет считывать последовательности измерений.
# В каждой последовательности нужно выбрать максимальное значение, а в итоге вывести 
# отсортированный по убыванию список этих макс значений, разделенных символом “;”.
# Во входных данных в первой строке будет задано целое положительное число – сколько
# записей нужно обработать, причем самих записей может быть больше чем это число, это
# нужно учесть. Значения в рамках одной записи разделены пробелом, минимальное число
# значений в записи – 1. Записи разделены переводом строки.
arr = []
for _ in range(int(input())):
    arr.append(max([int(i) for i in input().split()]))
arr.sort(reverse=True)
print(";".join([str(i) for i in arr]))

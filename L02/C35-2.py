# Необходимо написать программу, которая будет считывать со
# стандартного ввода строку и выводить уникальные символы, 
# встретившиеся в этой строке, в лексикографическом порядке
# по возрастанию. Символы из входа нужно приводить к нижнему
# регистру. Символ пробела не нужно учитывать при формировании
# результата. Выходные символы нужно разделять пробелом.
word = list(set(''.join(input().lower().split())))
word.sort()
print(' '.join(word))

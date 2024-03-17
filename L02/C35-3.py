# Необходимо написать программу, которая будет считывать со стандартного
# ввода строку. Нужно разбить строку на слова, словом будем считать
# последовательность символов отличных от пробелов (то есть знаки пунктуации
# будут входить в слова). Далее нужно посчитать сколько каждое слово
# встречалось в тексте и вывести наиболее часто слово и сколько оно
# встретилось. Все слова нужно также приводить к нижнему регистру при подсчете.
# Гарантируется, что в тексте самое частое слово – единственное.
text = input().lower().split()
words = list(set(text))
word = {i : 0 for i in words }
for w in text:
    word[w] += 1
out = max(word, key=word.get)
print(f'{out} {word[out]}')

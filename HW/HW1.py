# Необходимо написать программу, которая будет принимать на вход строку, разбивать
# строку на слова по пробелу. Далее нужно из всех слов убрать следующие пунктуационные знаки: 
# !,.?;:#$%^&*(),
# а также привести слова к нижнему регистру. В итоге нужно вывести в алфавитном порядке слова,
# которые состоят как минимум из 5 символов, а также имеют как минимум 4 уникальных символа,
# и которые встретились в исходном тексте более 2х раз.

# Ввели текст и произвели его преобразование и сокращение
NOT_USE = ['!', ',', '.', '?', ';', ':', '#', '$', '%', '^', '&', '*', '(', ')']
text = input().lower()
for s in NOT_USE:
    text = text.replace(s, '')
text = text.split()
new_text = [ word for word in text if len(word) >= 5 ]

# Подготовим слова
words = list(set(new_text))
words = { word : 0 for word in words }
for word in new_text:
    words[word] += 1
many_words = [ k for k, v in words.items() if v >= 3 ]
many_words.sort()

# Проверка букв
result = []
for word in many_words:
    b = set(word)
    if len(b) >= 4:
        result.append(word)

# Вывод
for word in result:
    print(word)

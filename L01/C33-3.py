# Необходимо написать программу, которая будет считывать со стандартного
# ввода строку, далее будет приводить ее к нижнему регистру, а также будет
# заменять символы “!”, “%”, “#”, “@” на пустую строку. В итоге нужно
# будет вывести в первой строке число замененных символов, а во
# второй преобразованную строку.
text = input().lower()
cnt = 0
cnt += text.count('!')
text = text.replace('!', '')
cnt += text.count('%')
text = text.replace('%', '')
cnt += text.count('#')
text = text.replace('#', '')
cnt += text.count('@')
text = text.replace('@', '')
print(cnt)
print(text)

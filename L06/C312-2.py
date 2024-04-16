# Написать функцию write_and_read, которая будет записывать в файл текст как параметр
# функции и читать текст из этого файла и передавать на выход функции.

# Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

import os

text = input()

def write_and_read(text):
    fn = os.path.join(os.path.abspath('/tmp'), 'test.txt')
    if not os.path.exists(fn):
        buffer = open(fn, 'w')
        buffer.close()
    with open(fn, 'w') as fp:
        fp.write(text)
    buf_str = ''
    with open(fn, 'r') as fp:
        buf_str = fp.read()
    if os.path.isfile(fn):
        os.remove(fn)
    return buf_str

print(write_and_read(text))


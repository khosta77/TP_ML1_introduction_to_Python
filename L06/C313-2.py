# Написать функцию fill_specializations, которая принимает список кортежей из специальности и имени
# и возвращает словарь, где в качестве ключей специальности, а в качестве значений - списки имен.
# Желательно, чтобы это было реализовано через словарь со значением по умолчанию.

# Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

from collections import defaultdict
from typing import List, Tuple


def fill_specializations(specializations: List[Tuple[str, str]]):
    result = {}
    for key, name in specializations:
        if not key in result:
            result[key] = []
        result[key].append(name)
    return result

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)


#specs=[('Sales', 'John Doe'), ('Sales', 'Martin Smith'), ('Accounting', 'Jane Doe'), ('Marketing', 'Elizabeth Smith'), ('Marketing', 'Adam Doe')]
#print(fill_specializations(specs))

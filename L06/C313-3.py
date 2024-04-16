# Написать функцию fill_missing_values, которая принимает два списка int-ов и делает из них
# один список кортежей, где в качестве элементов кортежа элементы списков на одинаковых позициях.
# Если один из список закончился, то в нужно заполнить значение в кортеже единицей.

# Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

from itertools import zip_longest
from typing import List, Tuple


def fill_missing_values(values_list_1: List[int], values_list_2: List[int]) -> List[Tuple[int, int]]:
    return [ (val1, val2) for val1, val2 in zip_longest(values_list_1, values_list_2, fillvalue=1) ]


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

# print(fill_missing_values([1, 2, 3], [2, 3, 4, 5]))

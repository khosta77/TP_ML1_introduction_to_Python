# Написать функцию rotate_list, которая принимает список целых чисел и целое число, которое будет задавать,
# сколько крутить список. Под кручением списка подразумевается забор элемента из конца списка и вставка
# его в начало списка. Желательно, чтобы это было реализовано через двустороннюю очередь.

# Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    if not nums:
        return []
    dq = deque(nums)
    for _ in range(n):
        dq.appendleft(dq.pop())
    return list(dq)

#'''
code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
#'''
#print(rotate_list([1,2,3,4], 5))

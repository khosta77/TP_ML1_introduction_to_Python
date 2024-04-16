# Написать функцию most_common_months, которая принимает в качестве параметра список строк,
# которые являются датами формата “ГГГГ-ММ-ДДTЧЧ-ММ-СС” и некоторое целое число n, и выводит
# топ n самых частых месяцев этих дат. Желательно, чтобы это было реализовано через Counter
# из модуля collections.

# Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
    months = [ int(date.split('-')[1]) for date in dates if len(date) >= 10 ]
    return [ month[0] for month in Counter(months).most_common(n) ]

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

#dates=["2023-01-01T23:59:59", "2023-01-01T23:59:59", "2023-02-01T23:59:59"]
#print(most_common_months(dates, 2))

# [1, 2]

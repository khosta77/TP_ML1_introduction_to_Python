#Реализуйте 3 метода в классе “Counter”:
#   __init__(self, initial_count) Этот метод нужен для инициализации класса с изначальным
#                                 параметром “изначальный подсчет”
#   increment(self) Этот метод должен делать +1 к нашему счетчику подсчетов
#   get(self) Этот метод должен возвращать подсчет

# Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

class Counter:

   def __init__(self, initial_count):
       self.a = initial_count

   def increment(self):
       self.a += 1

   def get(self):
       return self.a

#counter = Counter(0)
#counter.increment()
#print(counter.get())
#'''
code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
#'''

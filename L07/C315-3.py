# Реализуйте метод calculate_area в классе “Circle”, в котором уже есть атрибут класса pi,
# который понадобится для расчета: Этот метод будет рассчитывать площадь круга по формуле S=πR^2,
# где R передается в качестве параметра

# Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

class Circle:
   pi = 3.14

   def calculate_area(self, radius):
        return ( self.pi * ( radius ** 2 ) )

#circle = Circle()
#print(circle.calculate_area(2))
#'''
code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
#'''

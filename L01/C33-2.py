# Необходимо написать программу, которая будет считывать три числа
# и выводить их в определенном формате. Первое число целое, второе
# с плавающей точкой, третье целое неотрицательное. По примерам
# необходимо определить требуемый формат данных.
a = int(input())
b = float(input())
c = int(input())
print(f"{a:0=+10}")
print(f"{b:#>10.2f}")
res_current = (f"{(c):0>16b}")
res_current = str(res_current)
result = str(res_current)
result = (result[::-1])
print('_'.join(result[i:i+4] for i in range(0, len(result), 4))[::-1])

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


from random import uniform


n = int(input('Введите число: '))
array = {}
for i in range(1,n+1):
    array[i] = int (uniform(n, -n)) 
print (array)
for k in array:
    array[k] *= k
print (array)
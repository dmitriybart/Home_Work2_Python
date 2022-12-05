import random
 

lst = [1, 4, 5, 6, 3]
 
print ("Список: " + str(lst))
 

for i in range(len(lst)-1, 0, -1):
    j = random.randint(0, i + 1)
    lst[i], lst[j] = lst[j], lst[i]
print ("Перемешаный список : " +  str(lst))
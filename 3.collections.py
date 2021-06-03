# *** коллекции (контейнеры) ***

# список (list)

# создание пустого спска
my_list = []
my__list = list()

# добавление объекта (элемента) а список
my_list.append(100)
my_list.append(3.14)
my_list.append('hello')
my_list.append([10, 20, 30])

#print(my_list)

# чтение значений элемента 
# в квадратную кобочку указываем индекс
el = my_list[3]
el = my_list[3] [1]

#обратная  индексация

el = my_list[-1]

# замена значения элемента
my_list[0] = 2000


# удаление элемента по значению
# my_list.remove(3.14)

# удаление элемента по индексу
del my_list[-1]

# срез списка
s = 'hello, World'
my_list = list(s)

my_slice = my_list[2:5]
print(my_list)
print(my_slice)
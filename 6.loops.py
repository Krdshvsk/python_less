# *** ЦИКЛЫ ***

# оператор цикла while
# перевод как "пока"

#бесконечный цикл
#прерывается сочетанием калвиш Ctrl+c
# while True:
#     print('Hello')
# g = 10
# while g > 0:
#     print(f'HELLO{g}')
#     # g = g - 1
#     g -= 1


#иснтрукция прерывания цикала 
# по дополнительному условию
# g = 10
# while g > 0:
#     print(f'HELLO{g}')
#     if g == 5:
#         break
#     g -= 1

# оператор цикла for

#1. читает значение из иетрируемых объектов по порядку 
#2. значение присваивает в свою переменную 
#3. выполняет блок кода своего тела 

my_list = [10,20,30,40,50]
# в прямом порядке
# for i in my_list:
#     print(i)
#  впорядке наоборот 
# for i in my_list[:: -1]:
    # print(i)


# генератор списка 

# создание списка чисел в диапозоне от 10 до 100 с шагом 10
num_lst = [num * 2 for num in range(10, 100, 10)]

print(num_lst)
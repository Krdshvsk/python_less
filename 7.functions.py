# *** Функции ***

# встроенная функция ввода данных
# data = input('введите данные: ')

# print(f"Вы ввеели вот это - {data}")


# 1 вариант. Функция, принимающие данные (обладдающаяя аргументами)
def func_1(arg_1):
    s = arg_1 ** 2
    w = s + 10
    print(f"результат: {w}")
# вызов функции 
# func_1(1000)

def func_2(a, b, c):
    res = a + b + c
    res += 290
    print(res)

# func_2(120, 38, 1120)

# аргумент может иметь значения по умолчанию
def func_3(arg_1, arg_2=100):
    print(arg_1 * arg_2)
# func_3(20, 10)
# func_3(100)
# func_3(3.14)

# 2 вариант. Функции, возвращающая данные 
def func_4(arg_1, arg_2):
    res = arg_1 + arg_2
    return res

# d = func_4(10, 10)

def func_5(x, y):
    res_1 = x * y
    res_2 =  x / y
    return res_1, res_2, x

#первый способ приема данных
d_1 = func_5(28, 14)
# второй способ приема данных
a, b, c = func_5(28,14)
# print(d_1)
# print(d_1[0])
# print(d_1[2])

# print(a, b, c)
# print(b)

# *** безумынные функции (лямда-выражения, лямбда-функции)

# особенности: 
# - всегда обладают аргументами
# - всегда возваращает результат

# Пример 1. лямбда внутри генератора списка 
my_list = [(lambda arg_1: arg_1.upper())(i) for i in "hello"]
print(my_list)

# пример 2. словарь лямбда-выражений
my_lambdas = {
    "*": lambda arg_1, arg_2: arg_1 * arg_2,
    "+": lambda w, z: w + z
}

print(my_lambdas['+'](5, 2))
print(my_lambdas['*'](5, 2))
#  *** пример. Калькулятор ***

#  Функция обработчик 
def calculate(n1, n2, op):
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        result = n1 / n2
    else:
        result = f'что это такое?: {op}? :('
    return result


# цикл программы
while True:
    # ввод данных 
    cmd = input("Командуйте, мисс:) ")
    if cmd == "stop":
        print("Bye-bye!")
        break

    num_1 = int(input("Ведите 1 число:"))
    num_2 = int(input("Ведите 2 число:"))
    op = input('Введите название операции:')

    # обработка данных 
    result = calculate(num_1, num_2, op)

    # вывод данных 
    print(f"Результат: {result}")
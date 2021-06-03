#***логические операции***

z = 3
w = 2

# Операция 
# мы справшиваем 'значение z равно значению w?'
# Ответ (резульат)  будет присовоен переменной result
result = z == w

# операция "не равно"
result = z !=w 

#операция "меньше"
result = z < w 

#Операция "больше"
result = z > w

#операция менье или равно 
result = z <= w

#операци "больше или равно"
result = z >= w

#чистые логические операции 

var_1 = True
var_2 = True

# оператор "не" (NOT, инверция)
result = not var_1

#оператор "и" (AND)
#возвращает True только тогда, когда обе переменных
#являются True
result = var_1 and var_2


#оператор "или" (OR)
#возвращает False только тогда, когда обе переменных
#являются False
result = var_1 or var_2

#print(result)


#*** УСЛОВНЫЕ ОПЕРАТОРЫ***

# оператор "IF" (если)
#if True:
    #w = 'hello'
    #print(w)

z = 10

if z < 3:  #оператор "если"
    print('меньше')
else:  #оператор "иначе" 
    print('не меньше')

v = 'A'

if v == 'B':
    res = 'literal B'
elif v == 'A':
    res = 'literal A'
elif v == 'D':
    res = 'literal D'
elif v == 'W':
    res = 'literal W'
else:
    res = 'не понятный мне символ :('

print(res)
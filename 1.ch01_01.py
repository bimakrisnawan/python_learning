
# print("hello world from python")

# # syntax_code1 (gapake titik koma)

# # declare variables
# num = 2
# area = 58.7
# city = 'Berlin'
# country = "Germany"
# z = 10 + 5j # complex number

# # declare variable without initializing value
# counter = None
# index = None
# global var_global
# var_global = 10
# print(num)
# print(area)
# print(city)
# print(country)
# print(z)
# print(z.real)
# print(z.imag)
# print(var_global)


# a = 2.3
# b = 8
# c = a + b
# print(c)
# c = a - b
# print(c)
# c = a * b
# print(c)
# c = a / b
# print(c)

# MATHEMATICAL FUNC

# math.pow(x, y) adalah fungsi library Python bawaan yang mengembalikan nilai x ke pangkat y (x²).
# Metodesqrt () mengembalikan akar kuadrat dari jumlah x


# from math import *
# a = 1.8
# b = 2.5

# c = pow(a, b)
# print(c)

# c = sqrt(b)
# print(c)

# c = sin(a)
# print(c)

# print(pi)

# INCREMENT DECREMENT

# a = 4
# print(a)
# # increment
# a = a + 1
# print(a)
# a += 10
# print(a)
# # decrement
# a = a - 2
# print(a)
# a -= 7
# print(a)

# INPUT KEYBOARD

# Basically, the difference between raw_input and input is that the return type of raw_input 
# is always string, while the return type of input need not be string only.

# # getting input from keyboard using input()
# name = input('What is your name?')
# print('Hello,' + name + '!!')
# user_id = input('What is your ID?')
# print('Id is ' + str(user_id))
# # getting input from keyboard using raw_input()
# # ERROR bcs use pyhton 3.x
# product = input('Product name?')
# print('Product=' + product)
# product_id = input('Product ID?')
# print('Product id= ' + str(product_id))

# COMPARISON

# comparison operators
# a = 3
# b = 8
# print(a == b)
# print(a != b)
# print(a > b)
# print(a >= b)
# print(a < b)
# print(a <= b)
# # logical operators
# print((a == b) and (a != b))
# print((a <= b) or (a > b))
# print(not (a >= b))
# # bitwise operators
# # declare binary variables
# m = 0b01010011
# n = 0b11111001
# print(m)
# print(n)
# print(bin(m & n))
# print(bin(m | n))
# print(bin(m ^ n))
# print(bin(~m))
# print(bin(b << 3))
# print(bin(b >> 2))

# Decision

# a = 10
# b = 12

# # if, elif, else
# if(a == b) or (a == 10) and (b == 30):
#     print ("sama if")
# elif(a == b) or (a == 10) and (b == 12):
#     print ("sama elif")
# else:
#     print ("beda")

# # nested

# c = 20
# d = 50

# if(c==20):
#     if (d==50):
#         print ("masuk")
#     else:
#         print ("gagal masuk")
# else:
#     print("yah")
    
# # iteration
# # for
# print ("segitiga siku- siku")
# tinggi = input('Masukkan tinggi')
# for i in range (0, int(tinggi)):
#     for j in range (0, i):
#         print ("*", end="")
#     print ("*")

# # while
# print ("segitiga siku- siku(kebalik)")
# tinggi = input('Masukkan tinggi')
# a = int(tinggi)
# while a > 0 :
#     b = a
#     while b > 1:
#         print ("*", end="")
#         b -=1
#     print ("*")
#     a -=1

# BREAK, CONTINUE, PASS
# print('demo - break, continue and pass')
# for i in range(1, 10):
#     if i == 4:
#         continue
#     if i == 7:
#         break
#     print(i)

# pass # do nothing
# print('This is the end of program')
# CONTINUE = program lanjut tapi dilewati
# BREAK = program berhenti
# PASS = gangapa ngapain

# TIME

# import time
# # get current time
# now = time.time() # utc
# print(now)
# # display readable current time
# print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(now)))
# print(time.timezone)

# LIST

# # declare lists
# print('----declare lists')
# numbers = []
# a = [2, 7, 10, 8]
# cities = ['Berlin', 'Seattle', 'Tokyo', 'Moscow']
# b = [10, 3, 'Apple', 6, 'Strawberry']
# c = range(1, 10, 2)

# # print(lists
# print('----print(lists')
# print(a)
# for city in cities:
#     print(city)
# print(b)
# print(c)

# # get length of lists
# print('----get length of lists')
# print(len(a))
# print(len(cities))

# # add item into list
# print('----add item')
# numbers.append(10)
# numbers.append(5)
# print(numbers)
# cities.append('London')
# for i in numbers:
#     print(i)
# for city in cities:
#     print(city)

# # get specific item
# print('----get item')
# print(cities[2])
# print(a[3])

# # sorting
# print(a.sort())

# # edit item
# print('----edit item')
# cities[2] = 'new city'
# for city in cities:
#     print(city)

# # remove item
# print('----remove item')
# a.remove(8) # by value
# del cities[2] # by index
# for city in cities:
#     print(city)


# # tuples
# # declare tuples
# a = ()
# b = (3, 5, 7)
# c = ('Ford', 'BMW', 'Toyota')
# d = (3, (5, 'London'), 12)
# # print
# print(a)
# print(b)
# print(c)
# print(d)
# # get length of tuples
# print(len(a))
# print(len(b))
# print(len(c))
# print(len(d))
# # get item
# print(b[2])
# print(c[1])
# # get index
# print(b.index(7))
# print(c.index('Toyota'))


# DICTIONARY

# # declare
# a = {}
# b = {2: 'Sea', 3: 'River', 8: 'Mountain'}
# c = {2: {4: 'abcd', 5: 'hjkl'}, 3: 'vbnm'}
# d = dict(name='elena', age=30, roles=('manager', 'consultant'))
# # print
# print(a)
# print(b)
# print(c)
# print(d)
# # keys values
# print(b.keys())
# print(b.values())
# print(b.items())
# # add item
# a.setdefault(2, 'car')
# a.setdefault(5, 'train')
# a.setdefault(7, 'plane')
# print(a)
# # check key
# print(3 in b)
# print(8 in b)
# print(5 in b)


# # Function
# def penjumlahan (a,b):
#     c = a + b
#     # return c
#     print('hasilnya = ' + str(c))

# aa = input('Nilai a = ')
# aa = int(aa)
# bb = input('Nilai b = ')
# bb = int(bb)
# cc = penjumlahan (aa, bb)
# # print (cc)

# # MULTIPLE RETURN FUNC
# def perform(num):
#     d = num * 5
#     return d, d + 5, d - 2

# a = perform (5)
# print (a[2]) #kalo manggil semua ya tinggal gapake [], [] buat manggil index ke-

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
res = fibonacci(10)
print(res)









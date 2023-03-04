import random
from sys import getsizeof

'''
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/11-
Python%20Generators/02-Iterators%20and%20Generators%20Homework.ipynb
'''

# Task 1: Create a generator that generates the squares of numbers up to some number N.


def gensquares(numbers):
    for x in range(numbers):
        yield x**2


for num in gensquares(10):
    print(num)

print('\n')
# Task 2: Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library.


def rand_num(low, high, n):
    for number in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)


print('\n')
# Task 3: Use the iter() function to convert the string below into an iterator:

s = 'hello'

s_iter = iter(s)
print(s_iter)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

# Task 4: Explain a use case for a generator using a yield statement
# where you would not want to use a normal function with a return statement.

big_list = []
for n in range(10000):
    big_list.append(n)

print('big_list: ', getsizeof(big_list))


def big_data():
    for n in range(10000):
        yield n


big_gen = big_data()
print('big_gen: ', getsizeof(big_gen))


# Task 5: Can you explain what gencomp is in the code below?
# (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)

my_list = [1, 2, 3, 4, 5]
gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

print('gencomp: ', gencomp)

''' The upper code creates generator comprehension.
    The way of work is similar to the list comprehension but instead of list it created generator
    Below I present a list comp for the same range of values '''

listcomp = [item for item in my_list if item > 3]

for item in listcomp:
    print(item)

print('listcomp: ', listcomp)

#Beautiful Idiomatic approach to solve programming problems.
#1(if statement)
#hard
x = 1
y = 2
z = 3
if x <= y and y <= z:
    print("True")
#easy
if x <= y <= z:
    print ("True")

#2(Avoid placing conditional branch code on the same line as the colon)
#hard
name = 'Charan'
address = 'New York, NY'
if name: print(name)
print(address)
#easy
name = 'Charan'
address = 'New York, NY'
if name:
    print(name)
    print(address)

#3(Avoid repeating variable name in compound if statement)
#hard
name = 'Charan'
if name == 'Charan' or name == 'Nithin' or name == 'Rahul':
    is_generic_name = True
#easy
name = 'Charan'
is_generic_name = name in ('Charan', 'Nithin', 'Rahul')

#4(Use if and else as a short ternary operator replacement)
#hard
num = 0
f = True
if f:
    num = 1
    print(num)
#easy
f = True
num = 1 if f else 0
print(num)

#5(For loops)
#hard
list = ['steam','electric','disel']
index = 0
for element in list:
    print('{} {}'.format(index, element))
    index += 1
#easy
list = ['steam','electric','disel']
for index, element in enumerate(list):
    print('{} {}'.format(index, element))

#6(Use the in keyword to iterate over an iterable)
#hard
list = ['steam','electric','disel']
index = 0
while index < len(list):
    print(list[index])
    index += 1
#easy
list = ['steam','electric','disel']
for element in list:
    print(element)

#7(Use return to evaluate expressions in addition to return values)
#hard
a = 1
b = 2
c = 3
def all_equal(a,b,c):
    result = False
    if a == b == c:
        result = True
        print(result)
    return result
#easy
def all_equal(a,b,c):
    return a == b == c

#8(key word arguments)
#hard
def print_list(list, sep):
    print('{}'.format(sep).join(list))

list = ['Gates','Jobs','Jeff']
list_2 = ['microsoft','apple','amazon']
print_list(list, ' ')
print_list(list_2, ' ')
print_list(list_2, ', ')
#easy
def print_list(list, sep=' '):
    print('{}'.format(sep).join(list))

list = ['Gates','Jobs','Jeff']
list_2 = ['microsoft','apple','amazon']
print_list(list)
print_list(list_2)
print_list(list_2,', ')

#9(Use the function-based version of print)
#hard
print (1, 'Charan', __name__)
#easy
from __future__ import print_function
print(1, 'Charan', __name__)

#10(Use multiple assignment to condense variables all set to the same value)
#hard
x = 'Charan'
y = 'Charan'
z = 'Charan'
#easy
x = y = z = 'Charan'

#11(Avoid using a temporary variable when performing a swap of two values)
#hard
f = 'fun'
b = 'bun'
index = f
f = b
b = index
#easy
f = 'fun'
b = 'bun'
(f, b) = (b, f)

#12(Chain string functions to make a simple series of transformations more clear)
#hard
book_detailes = 'The Three Musketeers: Alexander Dumas'
formatted_book_detailes = book_detailes.strip()
formatted_book_detailes = formatted_book_detailes.upper()
formatted_book_detailes = formatted_book_detailes.replace(':', 'by')
#easy
book_detailes = 'The Three Musketeers: Alexander Dumas'
formatted_book_detailes = book_detailes.strip().upper().replace(':', 'by')

#13(Use ''.join when creating a single string for list elements)
#hard
result_list = ['psp', 'physics', 'maths']
result_string = ' '
for result in result_list:
    result_string += result
#easy
result_list = ['psp', 'physics', 'maths']
result_string = ' '.join(result_list)

#14(Use ord to get the ASCII code of a character and ord to get the character from an ASCII code)
hash_value = 0
character_hash = {
    'a': 97,
    'b': 98,
    'c': 99,
    #...
    'y': 121,
    'z': 122,
for e in some_string:
    hash_value += character_hash[e]
return hash_value
#easy
hash_value = 0
for e in some_string:
    hash_value += ord(e)
return hash_value

#15(Use a list comprehension to create a transformed version of an existing list)
#hard
list = range(10)
list2 = list()
for element in list:
    if is_prime(element):
        list2.append(element + 5)
#easy
list = range(10)
list2 = [element + 5
         for element in list
         if is_prime(element)]

#16(Make use of negative indexes)
#hard
def get_suffix(word):
    word_length = len(word)
    return word[word_length - 2:]
#easy
def get_suffix(word):
    return word[-2:]

#17(Prefer list comprehensions to the built-in map() and filter() functions.)
#hard
list = [1,2,3,4,5,6,7,8,9,10]
def odd(number):
    return number % 2 == 1
odd_numbers = filter(odd, list)
odd_numbers_times_two = list(map(lambda x: x * 2, odd_numbers))
#easy
list = [1,2,3,4,5,6,7,8,9,10]
odd_numbers_times_two = [n * 2 for n in list if n % 2 == 1]

#18(Use the built-in function sum to calculate the sum of a list of values)
#hard
list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for element in list:
    sum += element
#easy
list = [1,2,3,4,5,6,7,8,9,10]
sum = sum(list)

#19(Use all to determine if all elements of an iterable are True)
#hard
def containes_zero(iterable):
    for e in iterable:
        if e == 0:
            return True
    return False
#easy
def containes_zero(iterable):
    return not all(iterable)

#20(Prefer xrange to range unless you need the resulting list)
#hard
even_number = int()
for index in range (1000000):
    if index % 2 == 0:
        even_number = index
        break
#easy
even_number = int()
for index in xrange(1000000):
    if index % 2 == 0:
        even_number = index
        break

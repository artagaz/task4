#1
# my_list = input().split()
# list1 = [i for i in my_list if int(i) < 5]
# list2 = [int(i)/2 for i in my_list]
# list3 = [int(i)*2 for i in my_list if int(i) > 17]
# list4 = [i*i for i in range(0, int(input()))]
#print(*[int(i)*int(i) for i in input().split()])
#print(*[int(i)*int(i) for i in input().split() if int(i)%2 != 0 and str(int(i)*int(i))[-1] != '9'])
from idlelib.replace import replace


#2
#print(*['\n' + '*'*i for i in map(int, input().split())])

#3
# def triangle(x, y, z):
#     if x + y > z and x + z > y and y + z > x:
#         print('Это треугольник')
#     else: print('Это не треугольник')
#
# triangle(3,4,5)

#4
# from math import sqrt
# def distance(x1, y1, x2, y2):
#     print(sqrt(pow(x1-x2, 2) + pow(y1-y2, 2)))
#
# distance(0,0, 8,6)

#5
# from num2words import num2words
# def number_to_words(num):
#     try:
#         print(num2words(num, lang='ru'))
#     except NotImplementedError:
#         print(num2words(num, lang='en'))
#
# number_to_words(int(input()))

#6
# def bracket_check(test_str):
#     while "()" in test_str:
#         test_str = test_str.replace("()", "")
#     print('YES' if test_str == '' else 'NO')
#
# bracket_check('()()')

#7
# def palindrome(test_str : str):
#     a = test_str.replace(' ', '').lower()
#     if a == a[::-1]:
#         return 'Палиндром'
#     else:
#         return 'Не палиндром'
#
# print(palindrome('а роза упала на лапу Азора'))
# print(palindrome('не палиндром'))
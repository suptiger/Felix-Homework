'''
import os
a = os.path.dirname(os.path.abspath(__file__))
print(a)
print(__file__)
b = os.path.abspath(__file__)
print(b)
'''

def func1():
    print('1')

def func2():
    print('2')

def func3():
    print('3')

dic = {1:func1,2:func2,3:func3}

i = 4



try:
    dic[i]()
except:
    print('Please input 1-3')

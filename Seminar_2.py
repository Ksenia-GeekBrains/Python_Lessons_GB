""" lists=['222anton456', 'a1n1t1o1n1', '00000000a000n000t000o000n000' , 'gylfole','richard','ant0n']
print (lists)

for i in lists:
    if 'a' in i:
        if 'n' in i:
            if 't' in i:
                if 'o' in i:
                    if 'n' in i:
                        print(lists.index(i)+1) """

""" n = int(input())
list1 = []
for i in range(n):
    a = input()
    if 'a' in a:
        a = a[a.find('a'):]
        if 'n' in a:
            a = a[a.find('n'):]
            if 't' in a:
                a = a[a.find('t'):]
                if 'o' in a:
                    a = a[a.find('o'):]
                    if 'n' in a:
                        list1.append(i + 1)
print(*list1) """

""" a='opopoopppoooopppoooppppp'
max=0
for i in a:
        if i=="p":
            count+=1
        else:
            count=0
        if count>max:
            max=count
print(max) """

""" s=input()
t=0
while "P"*(t+1) in s:
    t+=1
if t!=0:
    print(t)
else:
    print(0) """


""" 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
*Пример:*
- Для N = 5: 1, -3, 9, -27, 81 """

""" n=int(input("Введите целое число: "))
start=[1]
count=1
a=1
while(count<n):
    start.append(a*(-3))
    a=(a*(-3))
    count+=1
print(start) """

""" numberN= int(input("Введите число N"))
for i in range(numberN):
    print((-3)**i) """


""" 2. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой. """

""" n='one'
list=['one','ghfjgfh','one', 'two','one','one']
print (list.count(n)) """

""" a = 'pyt'
b = 'pythonpythonpython'
count = 0
for i in range(0, len(b) - len(a)):
    if b[i:i + len(a)] == a:
        count += 1
print(count) """
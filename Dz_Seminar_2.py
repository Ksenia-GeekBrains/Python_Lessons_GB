""" 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11 """

""" from os import remove
n=float(input("Input Number: "))
m=str(n)
array=[i for i in m]
array.remove('.')
array2=[int(i) for i in array]
print(sum(array2)) """

""" 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

""" n=(int(input("Input Numbers ")))
factorial = 1
for i in range(2,n+1):
    factorial*=i
print(factorial) """

""" 3. Задайте список из n чисел последовательности (1+(1/n))^n и выведите на экран их сумму. """

""" n=(int(input("Input Numbers ")))
m=1
for i in range(1,n):
    m+=(1+(1/i))**i
print(round(m,3)) """

""" 3.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число. """

""" a= int (input('Введите число: '))
Numbers=[]
if a<0:
    i=1
    Numbers.append(a)
    while (i<=abs(a)*2):
        Numbers.append(a+i)
        i+=1
if a>=0:
    a=-a
    i=1
    Numbers.append(a)
    while (i<=(a*-2)):
        Numbers.append(a+i)
        i+=1
print(Numbers)

Position1=[]
Position2=[]
f=open("file.txt")
for line in f:
    Position1.append(line[0])
    Position2.append(line[2])

X1=int(Position1[0])
X2=int(Position2[0])

Y1=int(Numbers[X1])
Y2=int(Numbers[X2])

Product=Y1*Y2
print(Product) """

""" 4. Реализуйте алгоритм перемешивания списка. """

""" from random import randint


ListForMix=[1,2,3,4,5,6,7,8,9,10]
count=0
while(count<10):
    m=randint(0,len(ListForMix)/2)
    n=randint(len(ListForMix)/2,len(ListForMix)-1)
    temp=ListForMix[n]
    ListForMix[n]=ListForMix[m]
    ListForMix[m]=temp
    count+=1
print(ListForMix) """

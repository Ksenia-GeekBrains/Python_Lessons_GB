""" 1. Вычислить число c заданной точностью d
Пример:- при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10} """

""" d=0.001
Number=float(input('Введите число: '))
s=str(d)
p=int(abs(s.find('.') - len(s)) - 1)
FinalNumber=round(Number,p)
print(FinalNumber)
 """

""" 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N. """


""" N=670
Divider=2
Prime_factors=[]
Temp=N
while(Temp>1):
    if(Temp%Divider==0):
        Prime_factors.append(Divider)
        Temp=Temp/Divider
    else:
        Divider+=1
    
print(Prime_factors) """
    


""" 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. """

""" list= [42,25, 46, 89, 78, 25, 69, 85, 46]
list2=set(list)
Unique_list=[]
for i in list2:
    Unique_list.append(i)

print(Unique_list) """



""" 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 """
""" import random

k=2
a=random.randint(0, 100)
b=random.randint(0, 100)
c=random.randint(0, 100)
k=str(k)
a=str(a)
b=str(b)
c=str(c)
equation=a+'*x^'+ k+'+' + b+ '*x'+'+'+ c


with open('file.txt','w') as data:
    data.write(equation) """



""" 5.Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов. """
""" p1=''
p2=''
with open ('polynomial1.txt','r') as data1:
    p1=data1.read(-1)
with open ('polynomial2.txt','r') as data2:
    p2=data2.read(-1)

p1=p1.split('*')
p2=p2.split('*')
polynomial1=[]
for i in p1:
    polynomial1.append(int(i))
polynomial2=[]
for i in p2:
    polynomial2.append(int(i))
n1=len(p1)
n2=len(p2)
n=n1+n2-1
r=[0 for i in range(n)]
for k in range(n):
    for i in range(k+1):
        j=k-i
        if (j<n2) and (i<n1):
            r[k]+=polynomial1[i]*polynomial2[j]
m=str(sum(r))

with open('result.txt','w') as data:
    data.write(m) """
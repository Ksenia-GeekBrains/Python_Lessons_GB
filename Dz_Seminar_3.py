""" 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """

""" spisok=[2, 3, 5, 9, 3]
sum=spisok[1]
sum=0
i=1
while(i<len(spisok)):
    sum+=spisok[i]
    i+=2
print(sum)  """



""" 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] """

""" spisok=[2, 3, 5, 6]
spisok2=[]



if (len(spisok)%2!=0):
    i=0
    count=1
    while(i<(len(spisok)/2)):
        spisok2.append(spisok[i]*spisok[len(spisok)-count])
        i+=1
        count+=1
print(spisok2)
if (len(spisok)%2==0):
    i=0
    count=1
    while(i<(len(spisok)/2)):
        spisok2.append(spisok[i]*spisok[len(spisok)-count])
        i+=1
        count+=1
print(spisok2) """


""" 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 """

""" spisok=[1.1, 1.2, 3.1, 5, 10.01]
spisok2=[]
for i in spisok:
    if (i%1!=0):
        spisok2.append(round((i%1),2))
print(max(spisok2)-min(spisok2)) """


""" 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10 """

 

""" 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] """



""" LIST=[0,1]
K = 9
for i in range(1,K):
    LIST.insert(0,LIST[1]-LIST[0])
MAX_LIST_IND = len(LIST)
for i in range(1,K-1):
    LIST.insert(MAX_LIST_IND,abs(LIST[i-1]))
print(LIST) """
""" 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет """

""" DayOfWeek=int (input ("Введите число обозначающее день недели: "))
if (1<=DayOfWeek<=5):
    print("Не является выходным")
elif(6<=DayOfWeek<=7):
    print("Выходной")
elif (0<DayOfWeek>7):
    print("Не существует такой день недели") """


""" 2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. """

""" xyz=[5,0,5]

left = not (xyz[0] or xyz [1] or xyz [2])
right = not xyz[0] and not xyz[1] and not xyz [2]
if (left==right):
    print ("Утверждение истинно")
else:
    print("Утверждение ложно") """


""" Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 """

""" x= int(input("Введите Х не равное нулю: "))
y= int(input("Введите Y не равное нулю: "))

if (x ==0 or y==0):
    print("Введите Х и Y отличные от нуля")
elif (x>0 and y>0):
    print ("Точка находится в ПЕРВОЙ четверти оси координат")
elif (x<0 and y>0):
    print ("Точка находится во ВТОРОЙ четверти оси координат")
elif(x<0 and y<0):
    print ("Точка находится в ТРЕТЬЕЙ четверти оси координат")
elif(x>0 and y<0):
    print ("Точка находится в ЧЕТВЕРТОЙ четверти оси координат") """



""" 3.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y). """




""" x=int(input("Введите номер четверти (1,2,3,4) "))


if (x==1):
    print ("x ≥ 0 и y ≥ 0;")
elif (x==2) :
    print ("x ≤ 0 и y ≥ 0")
elif(x==3 ):
    print ("x ≤ 0 и y ≤ 0")
elif(x==4):
    print ("x ≥ 0 и y ≤ 0")
else:
    print ("Неверно введен номер четверти") """


""" Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. """
""" Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21 """





""" Xa=float (input("Введите X координаты первой точки"))
Xb=float (input("Введите Y координаты первой точки"))
Ya=float (input("Введите X координаты второй точки"))
Yb=float (input("Введите X координаты второй точки"))

C = (((Ya-Xa)**2+(Yb-Xb)**2))**0.5
print(round(C,2)) """

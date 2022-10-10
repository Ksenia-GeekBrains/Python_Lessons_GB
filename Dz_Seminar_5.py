""" #1.Напишите программу, удаляющую из текста все слова, содержащие ""абв"". """

""" with open("words.text", "r") as fin:
    for line in fin:
            words = line.split()
for word in words:
    if "abc" in word:
        words.remove(word)
sentence = " ".join(words)
print(sentence) """


""" Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
 """

from random import randint, random
from secrets import choice


""" Candy=2021
Player1=1
Player2=1
x=randint(0,1)
print(x)
if x==0:
    while(Player1>0 or Player2>0):
        if(Player1>0):
            Player1=Candy-randint(1,28)
            Candy=Player1
            print("Player1=")
            print(Player1)
        else:
            print("Player1 Winner")
            break
        if(Player2>0):
            Player2=Candy-randint(1,28)
            Candy=Player2
            print("Player2=")
            print(Player2)
        else:
            print("Player2 Winner")
            break
if x==1:
    while(Player1>0 or Player2>0):
        if(Player2>0):
            Player2=Candy-randint(1,28)
            Candy=Player2
            print("Player2=")
            print(Player2)
        else:
            print("Player2 Winner")
            break
        if(Player1>0):
            Player1=Candy-randint(1,28)
            Candy=Player1
            print("Player1=")
            print(Player1)
        else:
            print("Player1 Winner")
            break """


""" Создайте программу для игры в ""Крестики-нолики"". """

""" field= ["-","-","-","-","-","-","-","-","-"]
counter=0
move=choice(["X","O"])
while (counter<=8):
    temp=[]
    i=0
    while(i<len(field)):
        if(field[i]=="-"):
            temp.append(i)
        i=i+1
    x=randint(0,len(temp)-1)
    field[temp[x]]=move
    if((field[0] in ("X","O") and field[1] in ("X","O") and field[2] in ("X","O") and field[0]==field[1]==field[2])
    or(field[3] in ("X","O") and field[4] in ("X","O") and field[5] in ("X","O") and field[3]==field[4]==field[5])
    or(field[6] in ("X","O") and field[7] in ("X","O") and field[8] in ("X","O") and field[6]==field[7]==field[8])
    or(field[0] in ("X","O") and field[3] in ("X","O") and field[6] in ("X","O") and field[0]==field[3]==field[6])
    or(field[1] in ("X","O") and field[4] in ("X","O") and field[7] in ("X","O") and field[1]==field[4]==field[7])
    or(field[2] in ("X","O") and field[5] in ("X","O") and field[8] in ("X","O") and field[2]==field[5]==field[8])
    or(field[0] in ("X","O") and field[4] in ("X","O") and field[8] in ("X","O") and field[0]==field[4]==field[8])
    or(field[2] in ("X","O") and field[4] in ("X","O") and field[6] in ("X","O") and field[2]==field[4]==field[6])):
        print("Выиграл")
        print(move)
        print(field[0],field[1],field[2])
        print(field[3],field[4],field[5])
        print(field[6],field[7],field[8])
        exit()
    print(field[0],field[1],field[2])
    print(field[3],field[4],field[5])
    print(field[6],field[7],field[8])
    print()
    if (move=="X"):
        move="O"
    else:
        move="X"
    counter=counter+1
print("Боевая ничья")
print(field[0],field[1],field[2])
print(field[3],field[4],field[5])
print(field[6],field[7],field[8]) """


""" Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах. """


""" def encode(text):
    count = 1
    res = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res = res + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        res = res + str(count) + text[-1]
    return res

def decode(text):
    number = ''
    res = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            res = res + text[i] * int(number)
            number = ''
    return res


s = "LLLLLLGHKHGYGYGBNBGFJYUKJHUYULJJJJJJJJJJHHHHHHGGGGGGGGGDDDDDDDDD"
print(f"Текст после кодировки: {encode(s)}")
print(f"Текст после дешифровки: {decode(encode(s))}") """
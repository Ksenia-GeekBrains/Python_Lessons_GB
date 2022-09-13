dictionary = \
    {
        'a': 'а',
        'b': 'б',
        'v': 'в',
        'g': 'г',
        'd': 'д',
        'e': 'е',
        'zh': 'ж',
        'z': 'з',
        'i': 'и',
        'y': 'й',
        'k': 'к',
        'l': 'л',
        'm': 'м',
        'n': 'н',
        'o': 'о',
        'p': 'п',
        'r': 'р',
        's': 'с',
        't': 'т',
        'u': 'ю',
        'f': 'ф',
        'h': 'х',
        'c': 'ц',
        'ch': 'ч',
        'sh': 'ш',
        'shch': 'щ',
        'y:': 'ы',
        'e:': 'э',
        'yu': 'ю',
        'ya': 'я',
        ' ': ' ',
    }


""" value = 'shchuka'   
result=''
for i in value:
    result+=dictionary[i]

print(result) """

""" t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']
start_index = ord('а')
title = 'Переводим этот текст, сейчас!'


slug = ""
for s in title.lower():

    if "а" <= s <= "я":
        slug += t[ord(s) - ord('а')]
# elif s == "ё":
# slug = 'yo'
# elif s in " !?;:.,":
# slug = "-"
    else:
        slug += s

# while slug.count('--'):
# slug = slug.replace('--', '-')

print(slug) """

""" """ """ 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел. """
""" t="31 23 5 67 89 0 34 56 7 890"
list=[int(i) for i in t.split(' ')]
max=max(list)
min=min(list)
print(max,min) """




""" 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
1) с помощью математических формул нахождения корней квадратного уравнения
2) с помощью дополнительных библиотек Python """


""" A= 3
B=4
C=94
Discr=B**2-(4*A*C)
print(Discr,"Дискриминант")
if Discr<0:
    print("Действительных корней нет")
elif Discr==0:
    x=-B/(2*A)
    print(x,"Корень уравнения")
elif Discr>0:
    x=(-B + Discr**0.5)/(2*A)
    print(x,-x, "Квадратные корни уравнения") """

""" def discriminant(a: float, b: float, c: float) -> float:
    return b ** 2 - 4 * a * c


def solve_quadratic(a: float, b: float, c: float) -> str:
    if a == 0:
        raise ValueError("Not quadratic equation")
        
    d = discriminant(a, b, c)
    if d < 0:
        return "No roots"
    elif d == 0:
        return f"One root x = {-b / (2 * a)}"
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return f"Two roots: x1 = {x1}, x2 = {x2}"

if __name__ == "__main__":
    print(solve_quadratic(5, -9, -2))
    print(solve_quadratic(1, -4, 4))
    print(solve_quadratic(1, -5, 9))
    print(solve_quadratic(0, 1, 2)) """


""" 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел. """

""" A=10
B=120
X=0
i=2
while i<20:
    if A% i == 0 and B%i==0:
        X=i
        i+=1
        print(X) 
        break """
    
       


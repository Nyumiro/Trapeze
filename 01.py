def toVector(point_one, point_two):  # функция, создающая вектор по двум точкам. [0] -- по х, [1] -- по у
    return point_two[0] - point_one[0], point_two[1] - point_one[1]


def lenVector(vector):
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


def isParallel(vector_1, vector_2):
    det = vector_1[0] * vector_2[1] - vector_1[1] * vector_2[0]
    return det == 0


def Square(a1, a2, b1, b2):
    diag1 = toVector(a1, b2)
    diag2 = toVector(a2, b1)
    scalar_product = (diag1[0] * diag2[0]) + diag1[1] * diag2[1]
    len_1 = lenVector(diag1)
    len_2 = lenVector(diag2)
    if (len_1 * len_2) != 0:
        cos = scalar_product / (len_1 * len_2)  # находим косинус угла между диагоналями
        sin = (1 - cos * cos) ** 0.5  # находим синус через основное тригонометрическое тождество
        return 0.5 * len_1 * len_2 * sin  # находим площадь трапеции по формуле
    else:
        return -1


print("    B_____C")
print('   /       \\')
print("  A_________D")
# Проверку на корректность ввода решила не делать, чтобы не усложнять код.

print('Введите координату по х, нажмите Enter, затем введите координату по у.')
print('Точка A. Введите сначала координату по х, затем по у.')
b1 = (int(input()), int(input()))
print('Точка B. Введите сначала координату по х, затем по у.')
a1 = (int(input()), int(input()))
print('Точка C. Введите сначала координату по х, затем по у.')
a2 = (int(input()), int(input()))
print('Точка D. Введите сначала координату по х, затем по у.')
b2 = (int(input()), int(input()))

a1a2 = toVector(a1, a2)
b1b2 = toVector(b1, b2)
a1b1 = toVector(a1, b1)
a2b2 = toVector(a2, b2)

sides_len = [lenVector(a1a2), lenVector(b1b2), lenVector(a1b1), lenVector(a2b2)]  # массив длин сторон трапеции.

is_trapeze = (isParallel(a1a2, b1b2) ^ isParallel(a1b1, a2b2)) and 0 not in sides_len # xor -- чтобы код не переваривал прямоугольники и ромбы всякие, хотя они, вроде как, являются случаями трапеции.

isosceles = is_trapeze and (isParallel(a1a2, b1b2) and (lenVector(a1b1) == lenVector(a2b2))) or (
        isParallel(a1b1, a2b2) and (lenVector(a1a2) == lenVector(b1b2)))

perimeter = sum(sides_len)
square = Square(a1, a2, b1, b2)

print(f"Пункт 1. Заданная трапеция {'существует.' if is_trapeze else 'не существует.'} \n")
if is_trapeze:
    print(f"Пункт 2. Периметр заданной трапеции: {perimeter}. \n"
          f"Пункт 3. Заданная трапеция: {'равнобедренная.' if isosceles else 'неравнобедренная.'} \n"
          f"Пункт 4. Площадь заданной трапеции: {square}")

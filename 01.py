def toVector(point_one, point_two):  # функция, создающая вектор по двум точкам. [0] -- по х, [1] -- по у
    return point_two[0] - point_one[0], point_two[1] - point_one[1]


def lenVector(vector):  # функция, возвращающая длину заданного вектора
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


def isParallel(vector_1, vector_2):  # функция, проверяющая, параллельны ли векторы
    det = vector_1[0] * vector_2[1] - vector_1[1] * vector_2[0]
    return det == 0


def Square(a1, a2, b1, b2):
    diag1 = toVector(a1, b2)
    diag2 = toVector(a2, b1)
    scalar_product = (diag1[0] * diag2[0]) + diag1[1] * diag2[
        1]  # скалярное произведение векторов, представляющих собой диагонали трапеции
    len_1 = lenVector(diag1)  # длина первой диагонали
    len_2 = lenVector(diag2)  # длина второй диагонали
    if (len_1 * len_2) != 0:
        cos = scalar_product / (len_1 * len_2)  # находим косинус угла между диагоналями
        sin = (1 - cos * cos) ** 0.5  # находим синус через !основное тригонометрическое тождество!
        return 0.5 * len_1 * len_2 * sin  # находим площадь трапеции по формуле
    else:
        return -1


print('Точка а1. Введите сначала координату по х, затем по у')
a1 = (int(input()), int(input()))
print('Точка а2. Введите сначала координату по х, затем по у')
a2 = (int(input()), int(input()))
print('Точка б1. Введите сначала координату по х, затем по у')
b1 = (int(input()), int(input()))
print('Точка б2. Введите сначала координату по х, затем по у')
b2 = (int(input()), int(input()))

a1a2 = toVector(a1, a2)
b1b2 = toVector(b1, b2)
a1b1 = toVector(a1, b1)
a2b2 = toVector(a2, b2)

##1
is_трапеция = (isParallel(a1a2, b1b2) or isParallel(a1b1, a2b2)) and Square(a1, a2, b1, b2) > 0
##2
is_равнобедренная_трапеция = is_трапеция and (isParallel(a1a2, b1b2) and (lenVector(a1b1) == lenVector(a2b2))) or (
        isParallel(a1b1, a2b2) and (lenVector(a1a2) == lenVector(b1b2)))
##3
len_сторон = (lenVector(a1a2), lenVector(b1b2), lenVector(a1b1), lenVector(a2b2))
##4
периметр = sum(len_сторон)
##5
площадь = Square(a1, a2, b1, b2)

print(f"Пункт 1. Заданная трапеция {'существует.' if is_трапеция else 'не существует.'} \n")
if is_трапеция:
    print(f"Пункт 2. Периметр заданной трапеции: {периметр}. \n"
          f"Пункт 3. Заданная трапеция: {'равнобедренная.' if is_равнобедренная_трапеция else 'неравнобедренная.'}"
          f"Пункт 4. Площадь заданной трапеции: {площадь}")

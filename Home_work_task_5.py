#Напишите программу, которая принимает на вход координаты двух точек 
#и находит расстояние между ними в 2D пространстве.
#AB = √(xb - xa)2 + (yb - ya)2
def inputCoordinate(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        number = int(input(f"Введите координату по {xy[i]}: "))
        a.append(number)
    return a
print("Введите координаты точки А")
dotaA = inputCoordinate(2)
print("Введите координаты точки В")
dotaB = inputCoordinate(2)
length = ((dotaB[0] - dotaA[0]) ** 2 + (dotaB[1] - dotaA[1]) ** 2) ** (0.5)
print(f"Длина отрезка: {length}")
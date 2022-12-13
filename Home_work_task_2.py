#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
#(расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.
xyz = ["X", "Y", "Z"]
values = []
for i in range(3):
    values.append(input(f"Введите значение {xyz[i]}: "))
  
left = not (values[0] or values[1] or values[2])
right = not values[0] and not values[1] and not values[2]
result = left == right

if result == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")

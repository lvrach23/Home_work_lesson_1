#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
#и выдаёт номер четверти плоскости, в которой находится эта точка .
x = int(input("x="))
y = int(input("y="))
if x>0 and y>0:
    print('I')
elif x<0 and y>0:
    print('II')
elif x<0 and y<0:
    print('III')
elif x>0 and y<0:
    print('IV')
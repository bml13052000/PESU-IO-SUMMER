a=str(input("Enter values separated by comma: ")).split(",")
b=list(map(int,a))
print('Required list= ',b)
print('Required tuple= ',tuple(b))
# Задача 8: Требуется определить,
# можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

width = int(input('Введите ширину шоколадки :'))
length = int(input('Введите длину шоколадки :'))
desiredPiece = int(input('Введите сколько вы хотите отломить :'))
if desiredPiece%width==0 and desiredPiece<=width*length or desiredPiece%length==0 and desiredPiece<=width*length:
    print("Да вы можете отломить столько долек от шоколада одним разом")
else:
    print("Вы не сможете разломить шоколад на столько долек за один раз")
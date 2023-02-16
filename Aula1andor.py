x=int(input("Digite um número: "))
y=int(input("Digite um número: "))
z=int(input("Digite um número: "))

if x>y and x>z:
    r = "X é o maior número"
elif y>x and y>z:
    r="Y é o maior número"
elif z>x and z>y:
    r="Z é o maior número"
else:
    r="Há números iguais"
print(r)

    
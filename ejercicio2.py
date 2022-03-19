print("*****************")
print("Bienvenido al salpicon")
salpicon=[]

for i in range (1,11,1):
    fruta=input("Ingrese la fruta ")
    salpicon.append(fruta)
salpiconinverso = salpicon[::-1]
print("el salpicon tiene: ", salpiconinverso)

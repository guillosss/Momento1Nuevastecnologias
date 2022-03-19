print("***************")
print("Bienvenido al algoritmo para calcular multiplos")
contadormultiplos2=0
contadormultiplos3=0
cantidadNumeros=int(input("Cuantos numeros va ingresar"))
for cantidadNumeros in range (0,cantidadNumeros,1):
    numeroingresado = int(input("ingrese el numero: "));
    if (numeroingresado % 2 == 0):
        contadormultiplos2+=1
        
    if(numeroingresado % 3 == 0):
        contadormultiplos3+=1
    
    
print("el total de numeros ingresados multiplos de 2 fueron: ", contadormultiplos2, "el total de multiplos de 3 fueron: ",contadormultiplos3)



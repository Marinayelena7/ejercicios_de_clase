#Calcular el descuento
print("Dime el precio original del producto")
num1 = float(input())
print("Dime que porcentaje de descuento quieres aplicar? Del 5%, 10% o 20%")
num2 = int(input()) 
#Realizamos la operación

total = num1*(1-num2/100)
print("El precio final  es:", num1, "*",1, "-", num2,"/",100,"=", total, "euros") 
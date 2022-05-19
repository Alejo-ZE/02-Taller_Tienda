import math
cantidad = int(input("ingrese la cantidad que desea: "))
productos = ""
total = ()
for i in range(cantidad):
    producto = input("ingrese nombre del   producto:")
    precio = int(input("ingrese el precio del producto:"))
    productos += "%s $%i\n" % (producto, precio)
    total = int(cantidad * precio)

productos = productos[:len(productos)-1]


if total > 0 and total < 150000:
    descuento = 0
if total > 150000 and total < 300000:
    resultado = total
    descuento = (float(resultado))
elif total > 300000 and total < 700000:
    resultado = total * 0.15
    descuento = (float(resultado))
elif total > 70000:
    resultado = (total * 0.20)
    descuento = (float(resultado))
print("Centro Comercial Unaleño")
print("Compra más y Gasta Menos")
print("NIT: 899.999.063")
print(productos)
print("total: $", math.ceil(total-descuento), sep="")
print("En esta compra tu descuento fue $", (int(descuento)), sep="")
print("Gracias por tu compra ")
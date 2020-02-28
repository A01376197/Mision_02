# Autor: Michelle Ojeda Manjarrez, A01376197
# Descripcion: Calcular el costo total de una comida en un restaurante

# Escribe tu programa después de esta línea.

total_comida = int (input ("Costo de su comida: "))
propina = total_comida * .13
print ("Propina: $%.02f" % (propina))
iva = total_comida * .16
print ("IVA: $%.02f" % (iva))
total_pagar = total_comida + propina + iva
print ("Total a pagar: $%.02f" % (total_pagar))


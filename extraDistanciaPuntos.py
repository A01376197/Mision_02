# Autor: Michelle Ojeda Manjarrez, A01376197
# Descripcion: Encontrar la distancia entre dos puntos

# Escribe tu programa después de esta línea.

x1 = float (input ("x1: "))
y1 = float (input ("y1: "))

x2 = float (input ("x2: "))
y2 = float (input ("y2: "))

distancia = ((x2-x1)**2 + (y2-y1)**2 )**0.5

print ("Distancia: %.03f" % distancia)
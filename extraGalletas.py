# Autor: Michelle Ojeda Manjarrez, A01376197
# Descripcion: Calcular el número de ingredientes para cierto numero de galletas

# Escribe tu programa después de esta línea.

galletas = int (input ("¿Cuántas galletas quieres hacer?: "))
 
azucar = galletas * 1.5 / 48
mantequilla = galletas /48
harina = galletas * 2.75 /48

print ("Para %d galletas, se requiere: %.1f tazas de azúcar, %.1f taza de mantequilla y %.1f tazas de harina" % (galletas, azucar, mantequilla, harina))
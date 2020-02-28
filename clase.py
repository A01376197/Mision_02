# Autor: Michelle Ojeda Manjarrez, A01376197
# Descripcion: Calcular el porcentaje de hombres y mujeres inscritos en una clase

# Escribe tu programa después de esta línea.

mujeres_inscritas = int (input ("Mujeres inscritas: "))
hombres_inscritos = int (input ("Hombres inscritos: "))

total_alumnos = mujeres_inscritas + hombres_inscritos

print ("Total de inscritos: ", total_alumnos)

porcentaje_mujeres = mujeres_inscritas * 100/ total_alumnos

print ("Porcentaje de mujeres: %.01f%%" % (porcentaje_mujeres))

porcentaje_hombres = hombres_inscritos * 100/ total_alumnos

print ("Porcentaje de hombres: %.01f%%" % (porcentaje_hombres))
                         
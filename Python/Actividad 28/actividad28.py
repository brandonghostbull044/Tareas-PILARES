matricula = input('Ingresa tu matrícula: ')
calificaciones = input('Ingresa tus 5 calificaciones (separadas con cómas una de la otra): ')
promedio = (float(calificaciones.split(',')[0]) + float(calificaciones.split(',')[1]) + float(calificaciones.split(',')[2]) + float(calificaciones.split(',')[3]) + float(calificaciones.split(',')[4])) / 5

print(f'El alumno con la matricula "{matricula}" {"aprobó" if promedio >= 6 else "reprobó"} con un promedio de "{promedio}"')
try:
    f = open('archivoejempelo.txt')
    f.write('Linea de prueba dentor del archivo')
except:
    print('Algo paso al intentar abrir el archivo')
finally:
    f.close()
# Proyecto 3

Barredo Escalona Paola Betsabe 314135236
Sánchez Pérez Emiliano 316259408

Proyecto que cifra un documento y entrega n evaluaciones.
A partir de t evaluaciones descifra un documento previamente cifrado.

Para correr el programa es necesario:
-Conexión estable a internet
-Tener instalado Python3
-Contar con los archivos a cifrar y/o descifrar


#Instrucciones para ejecutar el programa:

En ./Proyecto3/src:

Para cifrar:
-> python3 main.py c evaluaciones.txt n t archivo_claro.txt

Donde:

evaluaciones.txt es el nombre del archivo donde se guardarán las n evaluaciones, se guardará en la carpeta "documentos" ( ./Proyecto3/src/documentos ) 

n es el número entero de evaluaciones que se generarán

t es el número entero mínimo de evaluaciones necesarias para descifrar

archivo_claro.txt es el nombre del archivo que se desea cifrar,debe encontrarse en la carpeta documentos ( ./Proyecto3/src/documentos ) 

Para descifrar:
-> python3 main.py d t_evaluaciones.txt archivo_claro.aes

Donde:

t_evaluaciones.txt es el nombre del archivo que contiene las t evaluaciones, debe encontrarse en la carpeta documentos (./Proyecto3/src/documentos)

archivo_claro.aes es el nombre del archivo a descifrar, al cifrarse se guardó en la carpeta documentos, por lo que debe encontrarse ahí  
(./Proyecto3/src/documentos)


Como ejemplo, en la carpeta documentos, se ha colocado un archivo llamado practica9.pdf, para cifrarlo la llamada sería:

En ./Proyecto3/src:

-> python3 main.py c evaluaciones.txt 20 10 practica9.pdf

También como ejemplo en la carpeta documentos se creó el archivo t_evaluaciones, el cual está vacío. Para ese caso se deben copiar al menos 10 de las 20 evaluaciones que se encuentran en el archivo evaluaciones.txt (el cual se creó al cifrar), y la llamada para el descifrado sería:

En ./Proyecto3/src:

-> python3 main.py d t_evaluaciones.txt practica9.aes





Instrucciones para ejecutar pruebas:

En ./Proyecto3/src/tests:

Para cifrado:
-> python3 -m unittest cifrado_test

Para descifrado:
-> python3 -m unittest descifrado_test

Donde: 
archivo_claro.txt y archivo_claro.aes:

Archivos para realizar las pruebas de cifrado_test.py

archivo_claro2.txt y archivo_claro2.aes:

Archivos para realizar las pruebas de descifrado_test.py

evaluaciones_prueba.txt:

Archivo para realizar ambas pruebas


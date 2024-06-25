print ("Empresa de gas \n  Gaxplosive\n")

import csv
def menu():
    i=0
    lista=[]
    lista2=[]
    lista3=[]


    while True:

        print ("1. Registrar pedido")
        print ("2. Listar pedido")
        print ("3. Imprimir hoja de ruta")
        print ("4. Salir del programa\n")

        opcion = input("Ingresar opción: \n")

        
        if opcion == "1":

            nombres = input ("Nombre: ")
            apellidos = input ("Apellido: ")
            comunas = input("Comuna: ")

            
            print ("Elija cuantos cilindros necesta")

            detalles_5s = int( input("Cilindro 5 kg: "))
            detalles_15s = int( input("Cilindro 15 kg: "))
            detalles_45s = int( input("Cilindro 45 kg: "))
            
      
            
            lista.append([nombres,apellidos, comunas, detalles_5s,detalles_15s,detalles_45s])
            print (lista)
            

            """with open('Gaxplosive.csv', 'w', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                # Escribir una fila en el archivo CSV
                escritor_csv.writerow(['Nombres','Apellidos', 'Comunas', 'Cil. 5kg','Cil. 15kg','Cil. 45kg'])
                # Escribir múltiples filas en el archivo CSV
                escritor_csv.writerows(lista)"""
        
        if opcion == "2":
            print ('Pedidos: \n ')
            print ('Nombres Apellidos Comunas Cil. 5kg Cil. 15kg  Cil. 45kg')
            for lineas in lista:
             print (lineas )
    
            
        if opcion == "4":
            break    

menu()



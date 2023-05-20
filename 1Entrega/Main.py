import json
import os

# Regristrarse
def Regristrarse():
    Nombre = input('Ingrese su Nombre: ')
    Contrasenia = input('Ingrese su Contraseña: ')
    if os.path.exists('Usuarios.json'):
        Lec = open('Usuarios.json', 'r')
        DB = dict(json.load(Lec))
        Lec.close()
        if Nombre in DB:
            return print(f'{Nombre} Ya se encuentra registrado debe iniciar sesion')
        else:
            AddData = {Nombre: Contrasenia}
            DB.update(AddData)
            Esc = open('Usuarios.json', 'w')
            json.dump(DB, Esc, indent=4)
            Esc.close()
            return print(f'{Nombre} Regitrado exitosamente')
    else:
        NewData = {Nombre: Contrasenia}
        Esc = open('Usuarios.json', 'w')
        json.dump(NewData, Esc, indent=4)
        Esc.close()
        return print(f'{Nombre} Regitrado exitosamente')


# Loguearse
def Loguearse():
    Nombre = input('Ingrese su Nombre: ')
    Contrasenia = input('Ingrese su Contraseña: ')
    Lec = open('Usuarios.json', 'r')
    DB = dict(json.load(Lec))
    Lec.close()
    lista= list(DB.keys())
    if lista.count(Nombre) == 1:
        if DB[Nombre] == Contrasenia:
            return print(f'{Nombre} bienvenido inicio sesion correctamente')
        else: 
            return print('Contraseña incorrecta')
    else:
        return print('Usuario no registrado')

# Ver Datos
def VerDatos():
    if os.path.exists('Usuarios.json'):
        try:
            Lec = open('Usuarios.json', 'r')
            DB = dict(json.load(Lec))
            Lec.close()
            for Usuario in DB:
                print(Usuario)
        except:
             return print('No hay usuarios registrados')
    else:
        return print('No hay usuarios registrados')
    
# Menu
Menu = True
while Menu :
    print('''
============================
            Menu
============================
Ingrese (1) para Registrarse
Ingrese (2) para Loguearse
Ingrese (3) para Ver Datos
Ingrese (4) para Salir
============================
''')
    try:
        Opcion = int(input('Ingrese un numero: '))
        if Opcion == 1:
            Regristrarse()
        elif Opcion == 2:
            Loguearse()
        elif Opcion == 3:
            VerDatos()
        elif Opcion == 4:
            Menu = False
            print('Hasta Luego')
        else:
            print('Opcion Invalida')
    except:
        print('Debe ingresar un numero')
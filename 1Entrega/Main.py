# Datos en Memoria

DB= {
        # 'dario': 'dario',
        # 'ema': 'ema',
        # 'rodriguez': 'rodriguez',
    }

# Regristrarse

def Regristrarse():
    Nombre = input('Ingrese su Nombre: ')
    Contrasenia = input('Ingrese su Contraseña: ')
    NewDatos = {f'{Nombre}': f'{Contrasenia}',}
    try:
        if len(DB) == 0:
            DB.update(NewDatos)
            return print(f'{Nombre} Regitrado exitosamente')
        else:
            Name = DB.get(Nombre, False)
            if Name and DB[Name] == Contrasenia:
                return print(f'{Nombre} Ya se encuentra registrado debe iniciar sesion')
            else:
                DB.update(NewDatos)
                return print(f'{Nombre} Regitrado exitosamente')
    except:
        return print('Ocurrio un error al registrarse')
    

# Loguearse

def Loguearse():
    Nombre = input('Ingrese su Nombre: ')
    Contrasenia = input('Ingrese su Contraseña: ')
    Name = DB.get(Nombre, False)
    try:
        if Name:
            if DB[Name] == Contrasenia:
                return print(f'Bienvenido {Nombre}')
            else:
                return print('Contraseña incorrecta')
        else:
            return print('Usuario no registrado')
    except:
        return print('Ocurrio un error al iniciar')

# Ver Datos

def VerDatos():
    for Clave in DB.keys():
        print(Clave)

# Menu
Menu = True
while Menu :
    print('''
Ingrese 1 para Registrarse
Ingrese 2 para Loguearse
Ingrese 3 para Ver Datos
Ingrese 4 para Salir
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
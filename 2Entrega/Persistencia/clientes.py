# class Clientes:
#     carrito = {}
    
#     def __init__(self, nombre, apellido, dni, telefono, email, pais):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.__dni = dni
#         self.__telefono = telefono
#         self.email = email
#         self.pais = pais
    
#     def __str__(self) -> str:
#         return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Telefono: {self.__telefono}, DNI: {self.__dni}, Pais: {self.pais}'
    
#     def comprar(self, producto, tienda):
#         if producto in self.carrito:
#             return print(f'El producto: {producto} ya se encuentra en el carrito.')
#         else:
#             self.carrito.update({producto : tienda})
#             return print(f'Producto agregado al carrito.')
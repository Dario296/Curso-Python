from Persistencia.clientes import Clientes

cliente1 = Clientes("dario", "rodriguez",39304699, 3512591067, "darioro@ya..", "arg")

print(cliente1)
print(cliente1.carrito)
cliente1.comprar("celular", "samsung")
cliente1.comprar("celular", "samsung")
cliente1.comprar("celular1", "motorola")
print(cliente1.carrito)
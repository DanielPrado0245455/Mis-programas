class Empleado:
  def __init__(self,nombre,puesto,antiguedad):
    self.nombre=nombre
    self.puesto=puesto
    self.antiguedad=antiguedad 
  def trabaja(self):
    print(self.nombre + " trabaja de " + self.puesto +       " desde hace " + str(self.antiguedad))
  
class Secretaria (Empleado):
  def __init__(self,nombre,puesto,tiempo):
    super().__init__(nombre,puesto,tiempo)
    self.sueldo=tiempo*15000
    print (self.sueldo," es su sueldo más bonos al año")
    
class Programador (Empleado):
  def __init__(self,nombre,puesto,tiempo):
    super().__init__(nombre,puesto,tiempo)
    self.sueldo=tiempo*25000
    print (self.sueldo," es su sueldo más bonos al año")

class Gerente (Empleado):
  def __init__(self,nombre,puesto,tiempo):
    super().__init__(nombre,puesto,tiempo)
    self.sueldo=tiempo*50000
    print (self.sueldo," es su sueldo más bonos al año")
  def aumentar(self,objeto):
    variable=int(input())
    objeto.sueldo+=variable



Trabajadores1=Gerente("Juan","Gerente",6)
Trabajadores1.trabaja()
print( " " )
Trabajadores2=Secretaria("Marta","Secretaria",5)
Trabajadores2.trabaja()
print( " " )
Trabajadores3=Programador("Roberto","Programador",4)
Trabajadores3.trabaja()
print( " " )

Trabajadores1.aumentar(Trabajadores2)
print(Trabajadores2.sueldo, " es el salario modificado")

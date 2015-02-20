from util import *
from Constantes import *
                        

#-----------------------------------------------------------------------
#Items
class Item(object):
	def __init__(self, item_id):
		self.idItem = item_id
		self.__cargarDatos()	

	def __cargarDatos(self):
		f = XML_OpenData("./scripts/Items.xml")
		self.Nombre = XML_GetItemName(f, self.idItem)
		self.Clase = 0xF
		self.Descripcion = XML_GetItemDescription(f, self.idItem)
		self.Usable = XML_GetItemUsable(f, self.idItem)
		self.Equipable = XML_GetItemEquipable(f, self.idItem)

class Pocion(Item):
	def __init__(self, item_id):
		Item.__init__(self, item_id)

	def Accion(self, personaje):
		personaje.HP += 25

class Eter(Item):
	def __init__(self, item_id):
		Item.__init__(self, item_id)
	
	def Accion(self, personaje):
		personaje.MP += 25

class Revive(Item):
	def __init__(self, item_id):
		Item.__init__(self, item_id)
	
	def Accion(self, personaje):
		personaje.isAlive = True
		personaje.HP = (1 * personaje.MaxHP) / 100

class Granada(Item):
	def __init__(self, item_id):
		Item.__init__(self, item_id)

	def Accion(self, personaje):
		personaje.HP -= 100

#-----------------------------------------------------------------------
#Armas
class Arma(object):
	def __init__(self, arma_id):
		self.idArma = arma_id
		self.Clase = 0x3
		self.__cargarDatos()
	
	def __cargarDatos(self):
		f = XML_OpenData("./scripts/Items.xml")
		self.Nombre = XML_GetWeaponName(f, self.idArma)
		self.Descripsion = XML_GetWeaponDescription(f, self.idArma)
		self.DanioF = XML_GetWeaponDamage(f, self.idArma)
		self.DanioM = XML_GeWeaponAbilityPower(f, self.idArma)
		

from util import *
from XML_util import *

class Personaje_Base(object):
	def __init__(self, nombre, cargar = False, f = None):
		if cargar:
			self.__cargarDatos(nombre, f)
		else:
			self.Nombre = nombre			
			self.lvl = 1
			self.ExpTope = 100
			self.ExpCurrent = 0
			self.HP_Max = 100
			self.HP_Current = 100 
			self.MP_Max = 50
			self.MP_Current = 50
			self.Atk_F = 15
			self.Atk_M = 10
			self.Def_F = 10
			self.Def_M = 10
			self.Speed = 15
			self.Evasion = 5
			self.Estado = None
			self.Alive = True			
			self.Inventario = []
			self.Skills = []
			
	def __cargarDatos(self, nombre, m_file):
		self.Nombre = nombre
		self.lvl = XML_GetLevel(m_file, nombre)
		self.ExpTope = XML_GetMaxExp(m_file, nombre)
		self.Exp = XML_GetExp(m_file, nombre)
		self.HP_Max = XML_GetHP(m_file, nombre)
		self.HP_Current = self.HP_Max
		self.MP_Max = XML_GetMP(m_file, nombre)
                self.MP_Current = self.MP_Max
		self.Atk_F = XML_GetAtkF(m_file, nombre)
		self.Atk_M = XML_GetAtkM(m_file, nombre)
		self.Def_F = XML_GetDefF(m_file, nombre)
		self.Def_M = XML_GetDefM(m_file, nombre)
		self.Speed = XML_GetSpeed(m_file, nombre)
		self.Evasion = XML_GetEvasion(m_file, nombre)		
		self.Inventario = XML_GetEquip(m_file, nombre)
		self.Skills = XML_GetSkills(m_file, nombre)
                self.cargarStats()

	def cargarStats(self, lista = None):
	        if lista is None:
                        for obj in self.Inventario:
                                if obj.Clase == 0x1 or obj.Clase == 0x2:        #Cabeza y Cuerpo
                                        self.HP_Max += obj.Vida
                                        self.HP_Current = self.HP_Max
                                        self.MP_Max += obj.Mana
                                        self.MP_Current = self.MP_Max
                                        self.Def_F += obj.Arm_F
                                        self.Def_M += obj.Arm_M
                                if obj.Clase == 0x3:                            #Armas
                                        self.Atk_F += obj.Danio
                                        self.Atk_M += obj.Magia
                                elif obj.Clase == 0x4 or obj.Clase == 0x5:      #Acce1 y Acce2
                                        self.HP_Max += obj.calcularHP(self.HP_Max)
                                        self.HP_Current = self.HP_Max
                                        self.MP_Max += obj.calcularMP(self.MP_Max)
                                        self.MP_Current = self.MP_Max
                                elif obj.Clase == 0x6:          #Botas
                                        self.Speed += obj.Speed
                                elif obj.Clase == 0x7:          #Items
                                        pass
	        else:
	                pass
	                
	def ataqueBasico(self, Malo):
		if sacarEvasion(Malo.Evasion):
			return "{0} ha esquivado el golpe!".format(Malo.Nombre)
		else:
			Damage = Malo.Def_F - self.Atk_F
			if Damage > 0:
				Damage = int((5 * self.Atk_F) / 100)
			Malo.getDamage(abs(Damage))			
			return "{0} ha recibido un daño de {1}".format(Malo.Nombre, Damage)

	def getDamage(self, damage):
		self.HP_Current -= damage
				

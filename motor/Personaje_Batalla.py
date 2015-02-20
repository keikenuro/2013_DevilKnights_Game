from util import *

class PersonajeBatalla(object):
        def __init__(self):
		#Interno:
                self.nombre = None
                self.lv = None
                self.hp = None
                self.mp = None
                self.atkF = None
                self.atkM = None
		self.defF = None
		self.defM = None
                self.speed = None
		self.isAlive = True		
		
		#Externo
		self.img = None
		self.areaDibujo = (100, 120, 100, 120)		
		self.paso = 0
		if os.name == 'nt':		
			self.delay = 60
		else:
			self.delay = 10

	def ataqueFisico(self, enemigo):
	        return enemigo.recibirDamage(ATK_FISICO, Rnd(self.atkF, self.atkF/2))
                
	def ataqueMagico(self, enemigo):
                return enemigo.recibirDamage(ATK_MAGICO, Rnd(self.atkM, self.atkM/2))
                
	def recibirDamage(self, id_atk, damage):
                ret = ""
		if id_atk == ATK_FISICO:
		        if sacarEvasion(self.speed):
		                ret = "Fallo!"
                        else:
                                if self.defF > damage:
                                        dmg = self.defF
                                else:
                                        dmg = damage - self.defF
                                self.hp -= dmg
                                ret = "{0} ha recivido {1} de danio!".format(self.nombre, dmg)                                
                else:
		        if sacarEvasion(self.speed):
		                ret =  "Fallo!"
                        else:
                                if self.defM > damage:
                                        dmg = self.defM
                                else:
                                        dmg = damage - self.defM
                                self.hp -= dmg
                                ret = "{0} ha recivido {1} de danio!".format(self.nombre, dmg)
                if self.hp <= 0:
                        ret = "{0} ha muerto!".format(self.nombre)
                        self.isAlive = False
                        
                return ret
                
        def setNombre(self, nombre):
                self.nombre = nombre
		self.img = loadImagen("./sprites/" + self.nombre + "_Sprites.png", True)
		self.img = pygame.transform.scale(self.img, (300, 480))
        
        def set_lv(self, lv):
                self.lv = lv
        
        def setHP(self, HP):
                self.hp = HP
        
        def setMP(self, MP):
                self.mp = MP

        def setSpeed(self, speed):
                self.speed = speed
                
        def setAtkF(self, atk_f):
                self.atkF = atk_f
        
        def setAtkM(self, atk_m):
                self.atkM = atk_m
        
	def setDefF(self, def_f):
		self.defF = def_f

	def setDefM(self, def_m):
		self.defM = def_m

        def clearAll(self):
               	self.nombre = None
               	self.lv = None
               	self.hp = None
               	self.mp = None
               	self.atkF = None
              	self.atkM = None
		self.speed = None
		self.defF = None
		self.defM = None

	def imprimir(self, win, x, y):
		win.blit(self.img, (x,y), self.areaDibujo)        

	def animar(self):
		if self.isAlive:
			if self.paso  == 0:
				self.areaDibujo = (self.areaDibujo[2], self.areaDibujo[1], self.areaDibujo[2], self.areaDibujo[3])
			elif self.paso == self.delay - 1:
				self.areaDibujo = (self.areaDibujo[0] + self.areaDibujo[2], self.areaDibujo[1], self.areaDibujo[2], self.areaDibujo[3])
			elif self.paso == self.delay * 2 - 1:			
				self.areaDibujo = (self.areaDibujo[2], self.areaDibujo[1], self.areaDibujo[2], self.areaDibujo[3])
			elif self.paso == self.delay * 3 - 1:
				self.areaDibujo = (0, self.areaDibujo[1], self.areaDibujo[2], self.areaDibujo[3])
			elif self.paso == self.delay * 4 - 1:
				self.paso = 0
			self.paso += 1
			#print self.paso

        def __str__(self):
                if self.nombre != None:
                        return "|" + self.nombre + "|Nivel: " + str(self.lv) + "|HP: " + str(self.hp) + \
                        "|MP: " + str(self.mp) + "|"
                else:
                        return "Vacio"

class MaloBatalla(PersonajeBatalla):
	def __init__(self):
		PersonajeBatalla.__init__(self)
	
	def setNombre(self, nombre):
		self.nombre = nombre
		self.img = loadImagen("./sprites/malos/" + self.nombre + "_Sprites.png", True)
		self.img = pygame.transform.scale(self.img, (300, 480))
		self.areaDibujo = (0, 0, 100, 120)
		
        def ia_atk(self, enemigo):
                pass

class Boss(MaloBatalla):
        def __init__(self):
                MaloBatalla.__init__(self)
        
        def setNombre(self, Nombre):
		self.nombre = Nombre
		self.img = loadImagen("./sprites/malos/" + self.nombre + "_Sprites.png", True)
		self.img = pygame.transform.scale(self.img, (300, 480))
		self.areaDibujo = (0, 0, 100, 120)


#class MaloBatalla(PersonajeBatalla):
#        def __init__(self):
#                PersonajeBatalla.__init__(self)
#		self.tipo = "minor"
#                self.Tesoros = None
#
#	def setNombre(self, nombre):
#               self.nombre = nombre
#		self.img = pygame.transform.flip(loadImagen("./sprites/malos/" + self.nombre + "_Sprites.png", True), True, False)
#		if "minor" ==  self.tipo:		
#			self.img = pygame.transform.scale(self.img, (300, 480))
#			self.areaDibujo = (100, 120, 100, 120)
#		else:
#			self.img = pygame.transform.scale(self.img, (510, 800))
#			self.areaDibujo = (170, 200, 170, 200)
#
#	def ia_atk(self, enemigos):
#		while True:
#			i = Rnd(len(enemigos), 0)
#			if enemigos[i].isAlive:
#				if Rnd(1, 0):
#					self.ataqueFisico(enemigo[i])
#				else:
#					self.ataqueMagico(enemigo[i])
#				break
#	def setTipo(self, t):
#		self.tipo = t
#
#       def setTesoros(self, tesoros):
#              self.Tesoros = [int(i) for i in tesoros.split(",")]
#

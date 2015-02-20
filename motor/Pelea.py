from util import *
from Personaje_Batalla import *
from XML_util import *

def WinScreen(win):
	pass

def GameOverScreen(win):
	pass

class Batalla(object):
        def __init__(self, win, BG, malos):
                #Pantalla
                self.win = win
                
                #Listas
                self.Party = self.__cargarParty()
                self.Malos = self.__cargarMalos()
		self.Boss = self.__cargarBoss()                

                #Imagenes
                self.BG = pygame.transform.scale(loadImagen("./media/battle/BG/" + BG), (DIMS[0], DIMS[1]))
                self.imgInfo = pygame.transform.scale(loadImagen("./media/textbox.png"), (DIMS[0] - 50, 120))
                self.imgSelected = pygame.transform.scale(loadImagen("./media/Selected.png", True), (100, 125))
		self.info = None                

                #Fuentes
                self.Fuente = pygame.font.Font(None, 30)
                
                #Otros
		self.malos_pos = 0
                self.pos = 0
                self.pressed = False
		self.atk = False
                
        def imprimir(self, atk = False):
		if atk:
			self.win.fill((0,0,0))

		self.win.blit(self.BG, (0,0))
		if self.Boss is not None:
			x = (DIMS[0] - ((len(self.Malos) * 100) + 170))/2
		else:
			x = (DIMS[0] - (len(self.Malos) * 100))/2

		y = (DIMS[1] + 200)/2 - 120
		cont = 0

		for per in self.Malos:
			per.animar()
			per.imprimir(self.win, x, y)
			x += 100

		if self.Boss is not None:
			pass
	
		x = (DIMS[0] - self.imgInfo.get_width())/2
                y = DIMS[1] - self.imgInfo.get_height()
		self.win.blit(self.imgInfo, (x, y))
		
		if self.info is not None:
			if not atk:
                		x = (DIMS[0] - self.info.get_width())/2
                		self.win.blit(self.info, (x, y + 30))

        def run(self):
		self.info = self.Fuente.render(str(self.Party[0]), 1, (255,255,255))
                while True:
                        for e in pygame.event.get():
                                if e.type == QUIT:
                                        exit(0)
                        k = pygame.key.get_pressed()                     
			if k[K_RETURN] and not self.pressed:
				self.Ataque()
				if len(self.Malos) == 0:
					WinScreen(self.win)
					return
				self.malos_atacan()
				self.siguienteAtacante()
                        elif k[K_ESCAPE] and not self.pressed:
                                if sacarEvasion(self.Party[0].speed):
					return
				else:
					self.info = self.Fuente.render("No has podido escapar!", 1, (255, 255, 255))
                        self.pressed = k[K_LEFT] or k[K_RIGHT] or k[K_RETURN] or k[K_ESCAPE]
                        self.imprimir()
                        pygame.display.flip()

	def Ataque(self):
		pos = 0
		nPos = 0

		press = True
		if self.Boss is not None:
			boss = True
			x = (DIMS[0] - ((len(self.Malos) * 100) + 170))/2
		else:
			boss = False
			x = (DIMS[0] - (len(self.Malos) * 100))/2

		y = (DIMS[1] + 200)/2 - 125 - 1
		img = copy.copy(self.imgSelected)

		info = self.Fuente.render(str(self.Malos[0]), 1, (255, 255, 255))

		while True:
			for e in pygame.event.get():
				continue
			k = pygame.key.get_pressed()
			if k[K_LEFT] and not press:
				nPos = pos - 1
			elif k[K_RIGHT] and not press:
				nPos = pos + 1
			elif k[K_RETURN] and not press:
				if Rnd(1, 0):
					if pos > len(self.Malos) - 1:
						info = self.Fuente.render(self.Party[self.pos].ataqueFisico(self.Boss), 1, (255, 255, 255))
					else:
						info = self.Fuente.render(self.Party[self.pos].ataqueFisico(self.Malos[pos]), 1, (255, 255, 255))
						if not self.Malos[pos].isAlive:
							del self.Malos[pos]
							pos -= 1
						
				else:
					if pos > len(self.Malos) - 1:
						info = self.Fuente.render(self.Party[self.pos].ataqueMagico(self.Boss), 1, (255, 255, 255))
					else:
						info = self.Fuente.render(self.Party[self.pos].ataqueMagico(self.Malos[pos]), 1, (255, 255, 255))
						if not self.Malos[pos].isAlive:
							del self.Malos[pos]
							pos -= 1
			        self.imprimir(True)
			        self.win.blit(info,((DIMS[0] - info.get_width())/2, (DIMS[1] - self.imgInfo.get_height())+30))
        			pygame.display.flip()
				return
			
			if boss and nPos in range(len(self.Malos) + 1):
				pos = nPos
			elif not boss and nPos in range(len(self.Malos)):
				pos = nPos

			if pos > len(self.Malos) - 1:
				info = self.Fuente.render(str(self.Boss), 1, (255, 150, 105))
				img = pygame.transform.scale(self.imgSelected, (170, 205))
				y = (DIMS[1] + 200)/2 - 205	
			else:
				info = self.Fuente.render(str(self.Malos[pos]), 1, (255, 150, 105))
				img = pygame.transform.scale(self.imgSelected, (100, 125))
				y = (DIMS[1] + 200)/2 - 125
	
			self.imprimir(True)
			self.win.blit(img, (x + (pos * 100), y))
			self.win.blit(info,((DIMS[0] - info.get_width())/2, (DIMS[1] - self.imgInfo.get_height())+30))
			press = k[K_LEFT] or k[K_RIGHT] or k[K_RETURN]
			pygame.display.flip()

        def siguienteAtacante(self):
                nPos = self.pos + 1
                if nPos in range(len(self.Party)):
                        self.pos = nPos
		else:
			self.pos = 0
		self.info = self.Fuente.render(str(self.Party[self.pos]), 1, (255,255,255))

        def __cargarParty(self):
                xml_file = XML_OpenData("./scripts/Slot1.xml")
                id_Personajes = XML_GetNamesList(xml_file)
                ret = []
                aux = PersonajeBatalla()
                
                for p in id_Personajes:
                        aux.setNombre(p)
                        aux.set_lv(XML_GetLevel(xml_file, p))
                        aux.setHP(XML_GetHP(xml_file, p))
                        aux.setMP(XML_GetMP(xml_file, p))
                        aux.setAtkF(XML_GetAtkF(xml_file, p))
                        aux.setAtkM(XML_GetAtkM(xml_file, p))
                        aux.setSpeed(XML_GetSpeed(xml_file, p))
	             	aux.setDefF(XML_GetDefF(xml_file, p))
	            	aux.setDefM(XML_GetDefM(xml_file, p))
                        ret.append(copy.copy(aux))
                        aux.clearAll()

                return ret

        def __cargarMalos(self, list_malos = None):
                xml_file = XML_OpenData("./scripts/Malos.xml")
		ret = []
                if list_malos is None:
                        list_malos = []
                        aux_lst = XML_GetBadList(xml_file)
                        for i in range(2):
                               list_malos.append(aux_lst[Rnd(0, len(aux_lst))])

		aux = MaloBatalla()
                for m in list_malos:
			aux.setNombre(XML_GetBadName(xml_file, m))
			aux.setHP(XML_GetBadHP(xml_file, m))
			aux.setMP(XML_GetBadMP(xml_file, m))
			aux.setAtkF(XML_GetBadAtkF(xml_file, m))
			aux.setAtkM(XML_GetBadAtkM(xml_file, m))
			aux.setDefF(XML_GetBadDefF(xml_file, m))
			aux.setDefM(XML_GetBadDefM(xml_file, m))
			aux.setSpeed(XML_GetBadSpeed(xml_file, m))
			ret.append(copy.copy(aux))
			aux.clearAll()
			
		return ret

	def __cargarBoss(self):
		return None

	def malos_atacan(self):
		if self.Boss is not None:
			boss = True
		else:
			boss = False
		
		if self.malos_pos > len(self.Malos) - 1 and not boss:
			self.malos_pos = 0
		elif self.malos_pos > len(self.Malos) and boss:
			self.malos_pos = 0
		
		

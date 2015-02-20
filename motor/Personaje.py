from util import *	
from Pelea import *
from Eventos import *

BTN_NO_BTN = 0
BTN_ARRIBA = 1
BTN_ABAJO = 2
BTN_DER = 3
BTN_IZQ = 4 

class Personaje(object):
        def __init__(self, m, w, nombrePer = "./sprites/Nick_Sprites.png"):        
		#Dependencia
                self.mapa = m
		self.win = w	        

		#Posicionamiento
                self.pos = self.__setPos()
                self.x = (self.pos % self.mapa.Ancho) * 80
                self.y = (self.pos / self.mapa.Alto) * 80
		
		#Imagen
 		self.img = loadImagen(nombrePer, True)
		self.img = pygame.transform.scale(self.img, (int(96*2.5), int(128*2.5)))
		
		#Dibujo		
		self.xOrigen = 80
		self.yOrigen = 0

                #Animacion
                self.Delay = 60
                self.Paso = 0
                self.Animando = False
                self.ArgsAnimacion = [None, None]
	
		#Estados
		self.EstadoActual = PARADO_FRENTE                

                #Eventos
                self.hayEvento = False
		self.contPasosBatalla = 0
		self.pressed = False
		self.ultimo_evento = 0	

		#Party
		self.Party = []
        
        def __setPos(self):
                for i in range(len(self.mapa.Eventos)):
	                if self.mapa.Eventos[i] == EVT_INICIO:
	                        return i
              
        def __tratarOtroEvento(self):
                preguntarPersona(self.pos, self.mapa)
                
        def update(self, joy = None):
                k = pygame.key.get_pressed()

                if self.Animando:
                        self.animar()
                        return

                if (k[K_UP] and not self.pressed) or ((joy is not None) and (joy.get_axis(1) == -1.0)):
                        self.moverArriba()
                elif (k[K_DOWN] and not self.pressed) or ((joy is not None) and (joy.get_axis(1)  > 0)):
                        self.moverAbajo()
                elif (k[K_LEFT] and not self.pressed) or ((joy is not None) and (joy.get_axis(0) == -1.0)):
                        self.moverIzq()
                elif (k[K_RIGHT] and not self.pressed) or ((joy is not None) and (joy.get_axis(0) > 0)):
                        self.moverDer()
                elif (k[K_z] and not self.pressed) or ((joy is not None) and joy.get_button(3)):
                        self.__tratarOtroEvento()
		if joy is not None:
                	self.pressed =  k[K_z] | joy.get_button(3) #k[K_UP] | k[K_DOWN]| k[K_LEFT] | k[K_RIGHT] |
		else:
			self.pressed =  k[K_z] #k[K_UP] | k[K_DOWN]| k[K_LEFT] | k[K_RIGHT] |
                
        def moverDer(self):
		self.EstadoActual = 0x2
		self.xOrigen = 80
		self.yOrigen = 160
                if self.pos % self.mapa.Ancho == (self.mapa.Ancho-1) % self.mapa.Ancho:
                        return
                        
                nPos = self.pos + 1
                if nPos in range(len(self.mapa.Imagen)):
                        if self.mapa.Grilla[self.mapa.Imagen[nPos] - 1].pisable and not self.mapa.Eventos[nPos] == EVT_PERSONA_ENCONTRADA:
				self.pos = nPos
                                self.Animando = True
                                self.ArgsAnimacion[0] = 'x'
                                self.ArgsAnimacion[1] = 1.33
                                self.animar()
                                
        def moverIzq(self):
		self.EstadoActual = 0x1
		self.xOrigen = 80
		self.yOrigen = 80
                if self.pos % self.mapa.Ancho == 0:
                        return
                        
                nPos = self.pos - 1
                if nPos in range(len(self.mapa.Imagen)):
                        if self.mapa.Grilla[self.mapa.Imagen[nPos] - 1].pisable and not self.mapa.Eventos[nPos] == EVT_PERSONA_ENCONTRADA:
                                self.pos = nPos
                                self.Animando = True
                                self.ArgsAnimacion[0] = 'x'
                                self.ArgsAnimacion[1] = -1.33
                                self.animar()
                                
        def moverArriba(self):
		self.EstadoActual = 0x3
		self.xOrigen = 80
		self.yOrigen = 240        
                nPos = self.pos - self.mapa.Ancho
                if nPos in range(len(self.mapa.Imagen)):
                        if self.mapa.Grilla[self.mapa.Imagen[nPos] - 1].pisable and not self.mapa.Eventos[nPos] == EVT_PERSONA_ENCONTRADA:
                                self.pos = nPos
                                self.ArgsAnimacion[0] = 'y'
                                self.ArgsAnimacion[1] = -1.33
                                self.Animando = True
                                self.animar()
                                                
        def moverAbajo(self):
		self.EstadoActual = 0x0
		self.xOrigen = 80
		self.yOrigen = 0
                nPos = self.pos + self.mapa.Ancho
                if nPos in range(len(self.mapa.Imagen)):
                        if self.mapa.Grilla[self.mapa.Imagen[nPos] - 1].pisable and not self.mapa.Eventos[nPos] == EVT_PERSONA_ENCONTRADA:
                                self.pos = nPos
                                self.Animando = True
                                self.ArgsAnimacion[0] = 'y'
                                self.ArgsAnimacion[1] = 1.33
                                self.animar()
                        
        def animar(self):
                if self.Delay == self.Paso:
			self.coordinarMovimientos()
                        self.Animando = False
                        self.Paso = 0
                        self.x = ((self.pos%self.mapa.Ancho) * 80)
                        self.y = ((self.pos//self.mapa.Ancho) * 80)
                        self.mapa.moverVistaCamara(self.x, self.y)
                        self.ProcesarEvento(self.pos)
			self.__renovarEventosRandoms()
                        return             
		else:
                        if self.ArgsAnimacion[0] == 'x':
                                self.x += self.ArgsAnimacion[1]
                        else:
                                self.y += self.ArgsAnimacion[1]
                        self.mapa.moverVistaCamara(self.x, self.y)        
			self.coordinarMovimientos()                        
			self.Paso += 1        

        def coordinarMovimientos(self):
		if self.Paso == self.Delay:
			if self.EstadoActual == CAMINANDO_FRENTE_1:
				self.EstadoActual = 0x0
				self.xOrigen = 80
				self.yOrigen = 0
				return
			if self.EstadoActual == 0x7:								
				self.EstadoActual = 0x1
				self.xOrigen = 	80
				self.yOrigen = 80			
				return
			if self.EstadoActual == 0x9:
				self.EstadoActual = 0x2
				self.xOrigen = 80
				self.yOrigen = 160
				return
			if self.EstadoActual == 0xB:
				self.EstadoActual = 0x3
				self.xOrigen = 80
				self.yOrigen = 240
				return
		else:
			if self.Paso == 0:
				if self.EstadoActual == 0x0:
					self.EstadoActual = 0x5
					self.xOrigen = 160
					self.yOrigen = 0
					return
				if self.EstadoActual == 0x1:
					self.EstadoActual = 0x7
					self.xOrigen = 160
					self.yOrigen = 80
					return
				if self.EstadoActual == 0x2:
					self.EstadoActual = 0x9
					self.xOrigen = 160
					self.yOrigen = 160
					return
				if self.EstadoActual == 0x3:
					self.EstadoActual = 0xB
					self.xOrigen = 160
					self.yOrigen = 240
					return
			elif self.Paso == 19:
				if self.EstadoActual == 0x5:
					self.EstadoActual = 0x4
					self.xOrigen = 0
					self.yOrigen = 0
					return
				if self.EstadoActual == 0x7:
					self.EstadoActual = 0x6
					self.xOrigen = 0
					self.yOrigen = 80
					return
				if self.EstadoActual == 0x9:
					self.EstadoActual = 0x8
					self.xOrigen = 0
					self.yOrigen = 160
					return
				if self.EstadoActual == 0xB:
					self.EstadoActual = 0xA
					self.xOrigen = 0
					self.yOrigen = 240
					return
			elif self.Paso == 40:
				if self.EstadoActual == 0x4:
					self.EstadoActual = 0x5
					self.xOrigen = 160
					self.yOrigen = 0
					return
				if self.EstadoActual == 0x6:
					self.EstadoActual = 0x7
					self.xOrigen = 160
					self.yOrigen = 80
					return
				if self.EstadoActual == 0x8:
					self.EstadoActual = 0x9
					self.xOrigen = 160
					self.yOrigen = 160
					return
				if self.EstadoActual == 0xA:
					self.EstadoActual = 0xB
					self.xOrigen = 160
					self.yOrigen = 240
					return
				
	def __renovarEventosRandoms(self):
		if self.contPasosBatalla == 29:
			self.contPasosBatalla = 0
			for i in range(len(self.mapa.Eventos)):
				if (self.mapa.Eventos[i] == EVT_NOEVENT or self.mapa.Eventos[i] == EVT_BATALLA_SIMPLE):
					if sacarEvasion(33):					
						self.mapa.Eventos[i] = EVT_BATALLA_SIMPLE
					else:
						self.mapa.Eventos[i] = EVT_NOEVENT
		else:
			self.contPasosBatalla += 1
        
	def ProcesarEvento(self, pos):
                if self.mapa.Eventos[pos] == EVT_BATALLA_SIMPLE:
			batalla = Batalla(self.win, "Casa_Interior2.png", ([1, 2], [1]))
			batalla.run()
			self.mapa.Eventos[pos] = EVT_NOEVENT           
                  
                elif self.mapa.Eventos[pos] == EVT_PERSONA_ENCONTRADA:
                        self.mapa.eventoEncontrarPersona(pos)
                
                elif self.mapa.Eventos[pos] == EVT_TELEPORT:
                        self.pos = self.mapa.eventoTeleport(pos)
                        self.x = (self.pos % self.mapa.Ancho) * 80
                        self.y = (self.pos / self.mapa.Alto) * 80

		elif self.mapa.Eventos[pos] == EVT_HISTORIA:
			id_evento = get_event_id(self.mapa.id_mapa, pos)
			print id_evento
			if (id_evento != -1) and (id_evento == self.ultimo_evento + 1):
				correr_evento(id_evento, self.win)
			        self.ultimo_evento += 1

	def imprimir(self, w):
	        x = self.x - self.mapa.camara_X + 1
	        y = self.y - self.mapa.camara_Y + 1
                w.blit(self.img, (x, y), (self.xOrigen, self.yOrigen, 80, 80))


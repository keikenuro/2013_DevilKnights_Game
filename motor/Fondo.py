from util import *
from glob import glob
from time import sleep

class Tile(object):
        def __init__(self, id_tile, imgFile, pisable, Evento = None):
                self.id_tile = id_tile
                self.pisable = pisable
                self.img = imgFile
                if not pisable:
                        self.Evento = EVT_NOEVENT
                else:
                        self.Evento = Evento                        
        
        def cambiarPisable(self, _pisable):
                self.pisable = _pisable
        
class Fondo(object):
	def __init__(self, win, mapa = "./scripts/mapa/Mapa_1.map"):              
		self.TP = []
		self.win = win
		self.Ancho, self.Alto, self.Buffer, self.Grilla, self.Imagen = self.__cargarMapa(mapa)
		self.__pintarFondo()
		self.Musica = ""
		
		self.Eventos = self.__cargarEventos(mapa)
		
		mapa = mapa.split("/")
		self.nombre_mapa = mapa[len(mapa)-1]
		self.id_mapa = int(self.nombre_mapa[len("Mapa_"):len(self.nombre_mapa) - len(".map")])

		self.camara_X = 0
		self.camara_Y = 0
		
		self.camara_dX = 1
		self.camara_dY = 1                        

        def __cambiarMapa(self, idMapa):
                self.TP = []
                mapa = "./scripts/mapa/Mapa_"+ idMapa +".map"
                self.Ancho, self.Alto, self.Buffer, self.Grilla, self.Imagen = self.__cargarMapa(mapa)                
		self.__pintarFondo()
		self.Musica = ""
		self.Eventos = self.__cargarEventos(mapa)
		
		mapa = mapa.split("/")
		self.nombre_mapa = mapa[len(mapa)-1]
		self.id_mapa = int(self.nombre_mapa[len("Mapa_"):len(self.nombre_mapa) - len(".map")])                

		self.camara_X = 0
		self.camara_Y = 0
		
		self.camara_dX = 1
		self.camara_dY = 1                        
                
	def setNuevosEventos(self, Eventos):
		self.Eventos = Eventos
        
	def __setEvento(self, args, lista):
	        id_evento = int(args[0], 16)

                if "|" in args[1]:
                        argumento_evento = args[1].split("|")
                else:
                        argumento_evento = [args[1]]
                
                del args
                
                if hex(EVT_RANDOM) in argumento_evento:
                        for pos_ev in range(len(lista)):
                                if lista[pos_ev] == EVT_NOEVENT and self.Grilla[self.Imagen[pos_ev]-1].pisable:
                                        if Rnd(100, 1) == 27:
                                                lista[pos_ev] = id_evento
                else:
                        if id_evento == EVT_PERSONA_ENCONTRADA:
                                self.__eventoEncontrarPersona(argumento_evento)

			elif id_evento == EVT_OBJETO_SINUSO:
			        indice = int(argumento_evento[1])
			        lista[indice] = id_evento
				self.__eventoObjetoSinUso(argumento_evento)

			elif id_evento == EVT_TELEPORT:
			        indice = int(argumento_evento[0])
			        lista[indice] = id_evento
			        self.__eventoTeleport(argumento_evento)

		        elif id_evento == EVT_INICIO:
	                        lista[int(argumento_evento[0])] = id_evento

			elif id_evento == EVT_HISTORIA:
				lista[int(argumento_evento[1])] = id_evento

                        elif id_evento == EVT_MUSICA:
                                self.Musica =  "./media/BGM/" + str(argumento_evento[0]) + ".ogg"

                return lista

	def __eventoObjetoSinUso(self, args):
		id_obj = int(args[0], 16)
		pos = int(args[1])

	 	if id_obj == OBJ_SILLON_1:
			img1 = pygame.transform.scale(loadImagen("./tiles/Sillon1_a.png", True), (80, 80))
			img2 = pygame.transform.scale(loadImagen("./tiles/Sillon1_b.png", True, (31,31)), (80, 80))

			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
			self.Buffer.blit(img2, (x + 80, y))
	
		elif id_obj == OBJ_SILLA_1:
			img1= pygame.transform.scale(loadImagen("./tiles/Silla1.png", True),(72,80))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_MESA_1:
			img1= pygame.transform.scale(loadImagen("./tiles/Mesa1.png", True),(70,80))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_ESCALERA_1:
			img1= pygame.transform.scale(loadImagen("./tiles/Escalera1.png", True),(80,80))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_PUERTA_1:
			img1= pygame.transform.scale(loadImagen("./tiles/Puerta.png", False),(80,80))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_PUERTA_2:
			img1= pygame.transform.scale(loadImagen("./tiles/Puerta.png", False),(80,80))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_ALFOMBRA_1:
			img1= pygame.transform.scale(loadImagen("./tiles/Alfombra.png", False),(160,80))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_ALFOMBRA_2:
			img1= pygame.transform.scale(loadImagen("./tiles/Alfombra2.png", False),(80,160))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_ALFOMBRA_3:
			img1= pygame.transform.scale(loadImagen("./tiles/Alfombra3.png", False),(80,160))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_CAMA_1:
			img1= pygame.transform.scale(loadImagen("./tiles/Cama1.png", True),(160,200))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_CAMA_2:
			img1= pygame.transform.scale(loadImagen("./tiles/Cama2.png", True),(80,160))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_SILLA_2:
			img1= pygame.transform.scale(loadImagen("./tiles/Silla2.png", True),(75,85))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_VENTANA_1:
			img1= pygame.transform.scale(loadImagen("./tiles/Ventana1.png", True),(80,80))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_MESITA_1:
			img1= pygame.transform.scale(loadImagen("./tiles/Mesa2.png", True),(80,80))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_BIBLIOTECA_1:
			img1= pygame.transform.scale(loadImagen("./tiles/Biblioteca1.png", True),(160,160))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_MESACOCINA_1:
			img1= pygame.transform.scale(loadImagen("./tiles/MesaCocina1.png", True),(160,145))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_MESACOMEDOR:
			img1= pygame.transform.scale(loadImagen("./tiles/MesaComedor.png", True),(155,85))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_CUADRO1:
			img1= pygame.transform.scale(loadImagen("./tiles/Cuadro1.png", True),(120,60))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_CUADRO2:
			img1= pygame.transform.scale(loadImagen("./tiles/Cuadro2.png", True),(120,60))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_CUADRO3:
			img1= pygame.transform.scale(loadImagen("./tiles/Cuadro3.png", True),(60,60))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_CUADRO4:
			img1= pygame.transform.scale(loadImagen("./tiles/Cuadro4.png", True),(60,60))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)

			self.Buffer.blit(img1, (x,y))
		elif id_obj == OBJ_ESPEJO:
			img1= pygame.transform.scale(loadImagen("./tiles/Espejo.png", True),(60,60))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)
			self.Buffer.blit(img1, (x,y))

		elif id_obj == OBJ_TESORO1:
			img1= pygame.transform.scale(loadImagen("./tiles/Tesoro1.png", False),(70,70))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)
			self.Buffer.blit(img1, (x,y))

		elif id_obj == OBJ_TESORO2:
			img1= pygame.transform.scale(loadImagen("./tiles/Tesoro2.png", True),(80,80))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)
			self.Buffer.blit(img1, (x,y))

		elif id_obj == OBJ_MUEBLECOCINA_1:
			img1= pygame.transform.scale(loadImagen("./tiles/MuebleCocina1.png", True),(160,160))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)
			self.Buffer.blit(img1, (x,y))

		elif id_obj == OBJ_MUEBLECOCINA_2:
			img1= pygame.transform.scale(loadImagen("./tiles/MuebleCocina2.png", True),(120,160))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)
			self.Buffer.blit(img1, (x,y))
		
		elif id_obj == OBJ_MESACOCINA_2:
			img1= pygame.transform.scale(loadImagen("./tiles/MesaCocina3.png", True),(80,90))
			x = ((pos % self.Ancho) * 80) 
	                y = ((pos // self.Ancho) * 80)
			self.Buffer.blit(img1, (x,y))

	def __eventoEncontrarPersona(self, args):
	        id_personaje = int(args[0], 16)
	        id_posicion = int(args[1], 16)
	        pos = int(args[2])
	        
	        del args
	        
	        if id_personaje == ID_NICK[0]:
	                img = loadImagen("./sprites/Nick_Sprites.png", True)
	                img = pygame.transform.scale(img, (240, 320))

                x = ((pos % self.Ancho) * 80) - 80
                y = ((pos // self.Ancho) * 80)
                
                if id_posicion == PARADO_ATRAS:
                        self.Buffer.blit(img, (x,y), (80, 240, 80, 80))
        
        def __eventoTeleport(self, args):
                #struct_ref_map = {casillero_de_partida, ref_sig_mapa, casillero_de_llegada}
                struct_ref_map = [int(args[0]), args[1], int(args[2])]
                self.TP.append(struct_ref_map)
        
        def eventoTeleport(self, pos):
                for i in self.TP:
                        if pos == i[0]:
                                self.win.fill((0,0,0))
                                pygame.display.flip()
                                sleep(1)
                                self.__cambiarMapa(i[1])
                                return i[2]
   
	def __cargarEventos(self, mapa):
		eventos = mapa[0:len(mapa)-len(".map")] + ".evt"
		f = open(eventos, "rt")
		ret = f.readlines()
		f.close()

		del f, eventos, mapa

		eventos_cargados = []		
		for ln in ret:
			ln = ln.strip()
			eventos_cargados.append(ln.split(", "))

		Eventos = []
		cont = 0		
		for tile in self.Imagen:
                        Eventos.append(EVT_NOEVENT)

                for evento in eventos_cargados:
                        Eventos = self.__setEvento(evento, Eventos)
                return Eventos

	def __pintarFondo(self):
	        x = 0
	        y = 0
	        for e in self.Imagen:
	                self.Buffer.blit(self.Grilla[e-1].img, (x,y))
	                x += 80
	                if x >= 80*self.Ancho:
	                        x = 0
	                        y += 80
	                
	def __cargarMapa(self, mapa):
		f = open(mapa, "rt")
		aux = f.readlines()
		f.close()

		del f, mapa		

		Grilla = []
		
		i = 0
		ln = aux[i].strip()
		while not "|" in ln:
			ln = ln.split(", ")
			
			tile_id = int(ln[0])
			
			tile_file = loadImagen("./tiles/" + ln[1] + ".png")
			tile_file = pygame.transform.scale(tile_file, (int(32*2.5), int(32*2.5)))
			
			pisable = int(ln[2])
			
			Grilla.append(Tile(tile_id, tile_file, pisable))
			
			i += 1
			ln = aux[i].strip()
					       
		Alto = len(aux) - i
		Ancho = len(aux[i].strip().split("|"))
		
		Mapa = []
		for j in range(i, len(aux)):
			for elemento in aux[j].strip().split("|"):
		                Mapa.append(int(elemento))

		Buffer = pygame.Surface((Ancho*80, Alto*80)).convert()
		
		return Ancho, Alto, Buffer, Grilla, Mapa

        def update(self):
                self.camara_X += (self.camara_dX - self.camara_X) / 10.0
                self.camara_Y += (self.camara_dY - self.camara_Y) / 10.0

        def moverVistaCamara(self, x, y):
                self.camara_dX = x - DIMS[0]/2
                self.camara_dY = y - DIMS[1]/2
                self.__limitesCamara()

        def moverCamara(self, dx, dy):
                self.camara_dX += dx
                self.camara_dY += dy
                self.__limitesCamara()        

        def __limitesCamara(self):
                if self.camara_dX < 0:
                        self.camara_dX = 0
                
                if self.camara_dY < 0:
                        self.camara_dY = 0
                        
                if self.camara_dX + DIMS[0] > self.Buffer.get_width():
                        self.camara_dX = self.Buffer.get_width() - DIMS[0]
                
                if self.camara_dY + DIMS[1] > self.Buffer.get_height():
                        self.camara_dY = self.Buffer.get_height() - DIMS[1]
        
        def eventoEncontrarPersona(self, pos):
                from Control_Novela import Novela
                #print "Persona_" + self.nombre_mapa[0:len(".map")+1] + ".mtx"
                n = Novela(self.win, "Persona_" + self.nombre_mapa[0:len(".map")+1] + ".mtx")
                n.run()
                        
	def imprimir(self):
	        origen = (self.camara_X, self.camara_Y, DIMS[0], DIMS[1])
	        destino = (0, 0, DIMS[0], DIMS[1])
		self.win.blit(self.Buffer, destino, origen)

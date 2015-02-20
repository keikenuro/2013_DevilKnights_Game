#!/usr/bin/python
#-*-coding: iso-8859-1 -*-
from motor.util import *
from motor.Personaje import Personaje
from motor.Fondo import Fondo
from motor.Menu import MenuPausa
from motor.Control_Novela import Novela

def loadConfig():
        _file = open("./config", "r")
        lines = _file.readlines()
        for line in lines:
                if "!fullscreen" in line:
                        SCREEN = line.strip()
                        SCREEN = SCREEN[len("!fullscreen "):len(SCREEN)]
                        SCREEN = bool(int(SCREEN))
                        
                elif "!width" in line:
                        ANCHO = line.strip()
                        ANCHO = ANCHO[len("!width "):len(ANCHO)]
                        ANCHO = int(ANCHO)
                        DIMS[0] = ANCHO
                        
                elif "!height" in line:
                        ALTO = line.strip()
                        ALTO = ALTO[len("!width "):len(ALTO)]
                        ALTO = int(ALTO)
                        DIMS[1] = ALTO
                        
                elif "!on" in line:
                        SOUND = line.strip()
                        SOUND = SOUND[len("!on "):len(SOUND)]
                        SOUND = bool(int(SOUND))

                elif "!enable" in line:
                        JOYSTICK = line.strip()
                        JOYSTICK = JOYSTICK[len("!enable "):len(JOYSTICK)]
                        JOYSTICK = bool(int(JOYSTICK))

        return [SCREEN, SOUND, JOYSTICK]

def getCodes(_buffer_):
        k = pygame.key.get_pressed()
        if k[k_a]:
                _buffer_ += "a"
        elif k[k_b]:
                _buffer_ += "b"
        elif k[k_c]:
                _buffer_ += "c"
        elif k[k_d]:
                _buffer_ += "d"
        elif k[k_e]:
                _buffer_ += "e"
        elif k[k_f]:
                _buffer_ += "f"
        elif k[k_g]:
                _buffer_ += "g"
        elif k[k_h]:
                _buffer_ += "h"
        elif k[k_i]:
                _buffer_ += "i"
        elif k[k_j]:
                _buffer_ += "j"
        elif k[k_k]:
                _buffer_ += "k"
        elif k[k_l]:
                _buffer_ += "l"
        elif k[k_m]:
                _buffer_ += "m"
        elif k[k_n]:
                _buffer_ += "n"
        elif k[k_o]:
                _buffer_ += "o"
        elif k[k_p]:
                _buffer_ += "p"
        elif k[k_q]:
                _buffer_ += "q"
        elif k[k_r]:
                _buffer_ += "r"
        elif k[k_s]:
                _buffer_ += "s"
        elif k[k_t]:
                _buffer_ += "t"
        elif k[k_u]:
                _buffer_ += "u"
        elif k[k_v]:
                _buffer_ += "v"
        elif k[k_w]:
                _buffer_ += "w"
        elif k[k_x]:
                _buffer_ += "x"
        elif k[k_y]:
                _buffer_ += "y"
        elif k[k_z]:
                _buffer_ += "z"

        return _buffer_

def splash():
	w = pygame.display.set_mode(DIMS, NOFRAME)
	img = pygame.transform.scale(loadImagen("./media/Fondo_Principal.png"), DIMS)
	w.blit(img, (0,0))
	pygame.display.flip()
	time.sleep(Rnd(5, 1))

def prologo(win):
        pygame.mixer.init(44100)
        
        pelicula = pygame.movie.Movie("./media/movies/Op.mpg")
        pelicula.set_volume(1.0)
        pelicula.set_display(win, (0, 0, DIMS[0], DIMS[1]))

        pygame.mixer.music.load("./media/BGM/Heresy.mp3")
        pygame.mixer.music.set_volume(1.0)
        
        pelicula.play()
        pygame.mixer.music.play()
        
        while pelicula.get_busy():
                for e in pygame.event.get():
                        k = pygame.key.get_pressed()
                        if k[K_ESCAPE]:
                                pelicula.stop()
                                pygame.mixer.music.stop()
                                return
        pelicula.stop()
        pygame.mixer.music.stop()

class MenuPrincipal():
	def __init__(self):
	        Configs = loadConfig()
	        if Configs[2]:
		        try:
			        self.joystick = pygame.joystick.Joystick(0)
		        except Exception:
		                GUIError("No se detecto nada", "Error con el Joystick")
                else:
			self.joystick = None
			
	        if Configs[0]:
        		self.win = pygame.display.set_mode((DIMS[0], DIMS[1]), FULLSCREEN)
		else:
		        self.win = pygame.display.set_mode((DIMS[0], DIMS[1]))
	
		self.img = pygame.transform.scale(loadImagen("./media/menu/MenuPrincipal.png"), DIMS)
		pygame.display.set_caption("Devil Knights v0.5")
		pygame.display.set_icon(loadImagen("./media/Icon.png"))
                
		#Cursor
		self.cursor = loadImagen("./media/Cursor.png", True)
		self.x_cursor = (37.5 * DIMS[0]) / 100 #600
		self.y_cursor = (25 * DIMS[1]) / 100 #140
		self.pos_cursor = 0

		self.nSalir = False

                if Configs[1]:
                        self.Sound = True
                else:
                        self.Sound = False
                        
	def run(self):		
	        prologo(self.win)
	        
		if self.joystick is not None:
			self.joystick.init()

		while True:
			self.win.fill((0,0,0))
			for e in pygame.event.get():
				k = pygame.key.get_pressed()
				if e.type == QUIT:
					return
				if k[K_ESCAPE]:
					return
				elif k[K_DOWN] or ((self.joystick is not None) and self.joystick.get_axis(1) > 0):
					self.pos_cursor += 1
					if not (self.pos_cursor in range(5)):
						self.pos_cursor -= 1
				elif k[K_UP] or ((self.joystick is not None) and self.joystick.get_axis(1) == -1.0):
					self.pos_cursor -= 1
					if not (self.pos_cursor in range(5)):
						self.pos_cursor += 1
				elif k[K_RETURN] or ((self.joystick is not None) and self.joystick.get_button(1)):
					if self.pos_cursor == 0:
						self.Nuevo_Juego()						
					elif self.pos_cursor == 1:
						pass
					elif self.pos_cursor == 2:
						pass
					elif self.pos_cursor == 3:
                                                self.Salir()
					elif self.pos_cursor == 4:
						self.Creditos()

			if self.pos_cursor == 0:
				self.x_cursor = (70.83 * DIMS[0])/100 #680
				self.y_cursor = (24.107142857142858 * DIMS[1])/100 #135
			elif self.pos_cursor == 1:
				self.x_cursor = (70.83 * DIMS[0])/100
				self.y_cursor = (34.821428571428569 * DIMS[1])/100
			elif self.pos_cursor == 2:
				self.x_cursor = (70.83 * DIMS[0])/100
				self.y_cursor = (45.535714285714285 * DIMS[1])/100 #255
			elif self.pos_cursor == 3:
				self.x_cursor = (70.83 * DIMS[0])/100
				self.y_cursor = (57.142857142857146 * DIMS[1])/100 #320
			elif self.pos_cursor == 4:
				self.x_cursor = 0
				self.y_cursor = (89.285714285714292 * DIMS[1])/100 #500

			self.win.blit(self.img, (0,0))
			self.win.blit(self.cursor, (self.x_cursor, self.y_cursor))
			pygame.display.flip()

	def Nuevo_Juego(self):
		nSalir = True
		mapa = Fondo(self.win)
		
		if self.Sound:
        		musica = mapa.Musica
        		try:
        		        msc = pygame.mixer.Sound(musica)
                                msc.set_volume(1.0)
                                msc.play(loops = 9999)
		        except Exception:
		                pygame.display.quit()
		                GUIError("Problemas al cargar el archivo.","Error en el audio")
                else:
                        musica = ""
	                msc = None
		
		
		per = Personaje(mapa, self.win)
	
	        _buffer = ""
	
		n = Novela(self.win, "0.mtx")
		n.run()

		while(nSalir):
			for e in pygame.event.get():
				k = pygame.key.get_pressed()
				if e.type == QUIT:
					return
				if k[K_ESCAPE] or ((self.joystick is not None) and self.joystick.get_button(9)):
					if MenuPausa(self.win, self.joystick):
						msc.stop()
						return
			per.update(self.joystick)
			mapa.update()

			mapa.imprimir()
			per.imprimir(self.win)

                        if self.Sound:
                                if musica != mapa.Musica:
                                        musica = mapa.Musica
                                        if musica == "":
                                                msc.stop()
                                        else:
                                                msc.stop()
                                                try:
                                                        msc = pygame.mixer.Sound(musica)
                                                        msc.set_volume(1.0)
                                                        msc.play(loops = 9999)                
                                                        print "Otra cancion."
                                                except Exception:
                        		                pygame.display.quit()
                        		                GUIError("Problemas al cargar el archivo.","Error en el audio")

			pygame.display.flip()
			if os.name == 'nt':
				pygame.time.delay(10)

                        

	def Cargar_Juego(self):
		pass

	def Extras(self):
		pass

	def Salir(self):
        	pelicula = pygame.movie.Movie("./media/movies/GameOver.mpg")
                pelicula.set_volume(1.0)
                pelicula.set_display(self.win, (0, 0, DIMS[0], DIMS[1]))
                pelicula.play()

                while pelicula.get_busy():
                        pass
                pelicula.stop()
                self.win.fill((0,0,0))
		pygame.display.flip()
		time.sleep(1)
		exit(0)

	def Creditos(self):	
		fuente = pygame.font.Font(None, 30)

		texto = "Programacion, Diseno de Historia, Diseno de Personajes: Kevin N. \"Kei Kenuro\" Encinas V."
		texto2 = "Historia, Diseno de Personajes, Desarrollo de Stages: Juan N. \"Chaosweilder\" Dahms"
		texto3 = "Pulse \"Esc\" para regresar..."
		
		img = fuente.render(texto, 1, (255, 255, 255))
		img2 = fuente.render(texto2, 1, (255, 255, 255))
		img3 = fuente.render(texto3, 1, (255, 255, 255))

		while True:
			for e in pygame.event.get():
				k = pygame.key.get_pressed()
				if e.type == QUIT or k[K_ESCAPE]:
					return

			self.win.blit(img, ((DIMS[0] - img.get_width())/2, 40))
			self.win.blit(img2, ((DIMS[0] - img2.get_width())/2, 80))
			self.win.blit(img3, (DIMS[0] - img3.get_width(), DIMS[1] - img3.get_height()))
			pygame.display.flip()
	
if __name__ == "__main__":
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()
	pygame.mouse.set_visible(False)
	splash()
	M = MenuPrincipal()
	M.run()

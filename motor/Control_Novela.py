from util import *
from glob import glob

class Actor(object):
        def __init__(self, id_actor, nombre, img_inicial):
                self.id = int(id_actor)
                self.nombre = nombre
                self.img = loadImagen("./media/novel_actor/" + nombre + "/" + img_inicial, True)
                self.img = pygame.transform.scale(self.img, (300, DIMS[1]))
                self.visible = False
        
        def setVisible(self, visible):
                self.visible = visible
        
        def cargarNuevaImagen(self, img):
                self.img = loadImagen("./media/novel_actor/" + self.nombre + "/" + img, True)
                self.img = pygame.transform.scale(self.img, (300, DIMS[1]))

class Novela(object):
        def __init__(self, win, n_archivo = "Prologo.mtx"):
                self.win = win
                #print "./scripts/novel/" + n_archivo
                self.Script = FILE("./scripts/novel/" + n_archivo)
                
                self.BG = None
                self.ChatBox = loadImagen("./media/textbox.png")
                self.ChatBox = pygame.transform.scale(self.ChatBox, 
                                                     (DIMS[0] - 50, 100))
                                                                     
                self.FuenteTexto = pygame.font.Font(None, 25)
                self.FuenteNombre = pygame.font.Font(None, 30)
                
                self.Texto = [None, None]
                self.Actores = [0]
                
                self.pressed = False
        
        def run(self):
                nSalir = True
                        
                while nSalir:
                        for e in pygame.event.get():
                                k = pygame.key.get_pressed()
                                if e.type == QUIT or k[K_ESCAPE]:
                                        nSalir = False
                                #if k[K_c] and not self.pressed:
                                #        pygame.image.save(self.win, "Captura1.png")
                        if nSalir:
                                k = pygame.key.get_pressed()
                                if (k[K_z] or k[K_SPACE]) and not self.pressed:
                                        aux = True
                                        while aux:
                                                aux = self.__analizarLinea()
                                                if not aux and self.Script.EOF:
                                                        nSalir = False
                                                        break
                                                else:
                                                        self.__imprimir()
                                                        pygame.display.flip()
                        self.pressed = k[K_z] or k[K_SPACE]# or k[K_c]                                                       
                        pygame.display.flip()

        #Funcion incompleta --                         
        def __imprimir(self):
                if self.BG is not None:
                        self.win.blit(self.BG, (0,0))
                        
                chat_x = (DIMS[0] - self.ChatBox.get_width()) / 2
                chat_y = DIMS[1] - self.ChatBox.get_height()
                        
                x = (DIMS[0] - (300 * len(self.Actores))) / 2
                        
                for i in range(len(self.Actores)):
                        try:
                                if self.Actores[i].visible:
                                        self.win.blit(self.Actores[i].img, (x,0))
                        except Exception:
                                pass
                        
                if self.Texto[1] is not None:
                        self.win.blit(self.ChatBox, (chat_x, chat_y)) 
                        if i == 0:
                                self.win.blit(self.Texto[1], (chat_x+30, chat_y+45))
                                return
                                
                        if self.Actores[i].visible:
                                self.win.blit(self.Texto[0], (chat_x + 25, chat_y + 10))
                        else:
                                pass
                        self.win.blit(self.Texto[1], (chat_x+30, chat_y + 30))
        
        #Funcion incompleta -- faltan actores, desiciones y finales
        def __tratadoDeLinea(self, ln):
                id = ln[0:ln.find(":")]
                ln = ln[ln.find(":")+1:len(ln)].strip()
                                
                if id == "event":
                        if "loadText" in ln:
                                ln = ln[len("loadText")+1:len(ln)-1]
                                ln = ln.split("|")
                                return [id, "loadText", int(ln[0]), ln[1]]
			
			if "loadImg" in ln:
                                ln = ln[len("loadImg")+1:len(ln)-1]
                                ln = ln.split("|")
                                return [id, "loadImg", int(ln[0]), ln[1]]
                elif id == "actor":
                        ln = ln.split("|")
                        return [id, ln[0], ln[1], ln[2]]                                        
                return None 
        
        #Funcion incompleta -- faltan actores, desiciones y finales
        def __analizarLinea(self):
                ln = self.Script.leerLinea()
		if ln == "EOF":
			return False

                args = self.__tratadoDeLinea(ln)
		
		if args == None:
			return True
		
		if args[0] == "actor":
		        self.Actores.append(Actor(args[1], args[2], args[3]))
		        return True
		        
		if len(args) == 3:
			if args[1] != "END":
				return True
			else:
				self.__Final(args)
				return True

		if len(args) == 4:
			if args[1] == "loadText":
				self.__manejarTexto(args)
				return False
			else:
				self.__manejarImagen(args)
				return True                
        
        #Funcion incompleta -- falta actores
        def __manejarImagen(self, args):
                #id, "loadImg", int(ln[0]), ln[1]
		if args[2] == 0:
			self.BG = loadImagen("./media/bg_novel/" + str(args[3]))
		else:
		        if args[3] == "NULL":
		                self.Actores[args[2]].setVisible(True)
	                else:
	                        self.Actores[args[2]].cargarNuevaImagen(args[3])
                        
		        
        
        #Funcion incompleta -- falta actores
        #return [id, "loadText", int(ln[0]), ln[1]]
	def __manejarTexto(self, args):
	        if args[2] == 0:			
		        aux = self.FuenteTexto.render(unicode(args[3], 'utf_8'), 1, (255, 255, 255))
		        self.Texto[1] = aux
		        return		                		
	        elif self.Actores[args[2]].visible:
	                #print self.Actores[args[2]].nombre
	                aux = self.FuenteNombre.render(unicode(self.Actores[args[2]].nombre, 'utf_8'), 1, (255, 0, 0))
	                self.Texto[0] = aux
	        
	        #print args[3]        
	        if args[3] == " ":
	                self.Texto[1] = None
                else:
                        aux = self.FuenteTexto.render(unicode(args[3], 'utf_8'), 1, (255, 255, 255))
	                self.Texto[1] = aux
	                return

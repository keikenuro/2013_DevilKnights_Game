from util import *
from Menu import *

class Juego(object):
        def __init__(self):
                self.win = pygame.display.set_mode(DIMS)
                pygame.display.set_caption("DK Prueba y Error")
                
                self.MenuPrincipal = MenuPrincipal(self.win)
                self.MenuPausa = MenuPausa(self.win)
                #self.MenuCargar = MenuCargarPartida(self.win)
                #self.MenuGuardar = MenuGuardarPartida
                #self.MenuOpciones = MenuOpciones(self.win)
                #self.MenuExtras = MenuExtras(self.win)
                
                #self.MotorNovela = Novela(self.win)
                #self.MotorPelea = Batalla(self.win)
                #self.MotorMovimiento = Escenario(self.win)
                
        def run(self):
                nSalir = True
                while nSalir:
                        for e in pygame.event.get():
                                k = pygame.key.get_pressed()
                                if e.type == QUIT or k[K_ESCAPE]:
                                        nSalir = False
                                        break
                        ret = self.MenuPrincipal.update()
                        if ret == NUEVO_JUEGO:
                                self.__main()
                        elif ret == CARGAR_JUEGO:
                                self.__main(self.MenuCargar.run())
                        elif ret == MENU_OPCIONES:
                                #self.MenuOpciones.run()
                                pass
                        elif ret == MENU_EXTRAS:              
                               #self.MenuExtras.run()
                               pass
                        elif ret == SALIR:
                                nSalir = False
                        elif ret == __ERROR_UNKNOW:
                                raise SystemExit, "No se que paso, lol"          
        
        def __main(self, *args):
                fondo = Escenario(self.win)
                per = Personaje(fondo)
                if len(args) != 0:
                        fondo.cargarGuardado(args[0])
                        per.cargarGuardado(args[1])
                
                nSalir = True
                while nSalir:
                        for e in pygame.event.get():
                                k = pygame.key.get_pressed()
                                if e.type == QUIT:
                                        nSalir = False
                                        break
                        if k[K_ESCAPE]:
                                ret = self.MenuPausa.run()
                                if not ret:
                                        nSalir = False
                                        break
                        per.update()
                        fondo.update()
                        
                        per.imprimir(self.win)

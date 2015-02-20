import pygame, os, sys, random, time
from pygame.locals import *
from Constantes import *
from xml.dom import minidom
from glob import glob
import copy
import Tkinter, tkMessageBox

def GUIError(mensaje, titulo):
        ven = Tkinter.Tk()
        ven.wm_withdraw()
        tkMessageBox.showerror(title = titulo, message = mensaje, parent = ven)
        exit(0)

def Rnd(M, m):
        return int(((M - m + 1) * random.random()))

def loadImagen(filename, transp = False, xy = (0,0)):
        try: 
                img = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        img = img.convert()
        if transp:
                color = img.get_at(xy)
                img.set_colorkey(color, RLEACCEL)
        return img                                

def sacarEvasion(maxEvasion):
	resultados = []
	cont = 0
	
	while cont != maxEvasion:
		aux = Rnd(100, 1)
		if aux in resultados:
			continue
		else:
			resultados.append(aux)
			cont += 1
	
	if Rnd(100, 1) in resultados:
		return True
	else:
		return False

class FILE():
        def __init__(self, nombre):
                self.fileName = nombre
                self.File = open(nombre, "r")
                self.current_ln = 1
                self.EOF = False
                
        def setLinea(self, d = 0):
                if d == 0:
                        self.current_ln += 1
                else:
                        temp = open(self.fileName, "r")
                        aux = 1
                        while (aux < d):
                                reg = temp.readline()
                                reg = reg.strip() 
                                if reg == "EOF":
                                        temp.close()
                                        return
                                else:
                                        aux += 1                
                        self.current_ln = d
                        self.File = temp
                         
        def setEOF(self):
                self.EOF = True
                
        def leerLinea(self):
		if not self.EOF:
                	reg = self.File.readline()
                	reg = reg.strip()
                	self.setLinea()
                	if "EOF" in reg:
                        	self.setEOF()
                        	return "EOF"
                	else:
                        	return reg
        	return "EOF"

        def cerrarArchivo(self):
                self.File.close()


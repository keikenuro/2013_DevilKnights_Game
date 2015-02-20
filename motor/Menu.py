from util import *

def MenuPrincipal(win):
	fondo_img = pygame.transform.scale(loadImagen("./media/menu/MenuPrincipal.png"), DIMS)
	cursor_img = loadImagen("./media/Cursor.png", True)
	pos = 0
	pressed = False
	nSalir = True
	
	while nSalir:
		e = pygame.event.get()
		k = pygame.key.get_pressed()

		

def MenuPausa(win, joy = None):
	fondo = copy.copy(win)
	img_Menu = loadImagen("./media/MenuPausa.png")
	img_Cursor = loadImagen("./media/Cursor.png", True)
	yCursor = 335
	pos = 0
	nSalir = True
	pressed = False
	press = False
	while nSalir:
		win.fill((0,0,0))
		for e in pygame.event.get():
			k = pygame.key.get_pressed()
			press = False
			if (k[K_UP] or ((joy is not None) and (joy.get_axis(1) == -1.0))) and not pressed:
				npos = pos - 1
				if npos in (0,1):
					pos = npos
					yCursor -= 120
				press = True
				
			elif (k[K_DOWN] or ((joy is not None) and (joy.get_axis(1) > -1.0))) and not pressed:
				npos = pos + 1
				if npos in (0,1):
					pos = npos
					yCursor += 120
				pres = True

			if k[K_RETURN] or ((joy is not None) and (joy.get_button(1))):
				if pos == 0:
					return 0
				else:
					return 1

			pressed =  press or k[K_DOWN] or k[K_UP]
			
		win.blit(fondo, (0,0))
		win.blit(img_Menu, ((DIMS[0] - img_Menu.get_width())/2 , 0))
		win.blit(img_Cursor, ((DIMS[0] - img_Menu.get_width())/2 - 20, yCursor))
		pygame.display.flip()

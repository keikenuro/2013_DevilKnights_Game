from Constantes import *
from util import *

def preguntarPersona(pos, mapa):
        try:
                nPos = pos + 1
                if mapa.Eventos[nPos] == EVT_PERSONA_ENCONTRADA:
                        mapa.eventoEncontrarPersona(nPos)
                        return
        except Exception:
                pass

        try:
                nPos = pos - 1
                if mapa.Eventos[nPos] == EVT_PERSONA_ENCONTRADA:
                        mapa.eventoEncontrarPersona(nPos)
                        return
        except Exception:
                pass
                
        try:
                nPos = pos + mapa.Ancho
                if mapa.Eventos[nPos] == EVT_PERSONA_ENCONTRADA:
                        mapa.eventoEncontrarPersona(nPos)
                        return
        except Exception:
                pass
        
        try:
                nPos = pos - mapa.Ancho
                if mapa.Eventos[nPos] == EVT_PERSONA_ENCONTRADA:
                        mapa.eventoEncontrarPersona(nPos)
                        return
        except Exception:
                pass

def preguntarTeleport(pos, mapa):
        if mapa.Eventos[pos] == EVT_TELEPORT:
                mapa.eventoTeleport(pos)
                return

def correr_evento(id_evento, win):
	win.fill((0,0,0))
	pygame.display.flip()

	from Control_Novela import Novela
	
	n = Novela(win, str(id_evento) + ".mtx")
	n.run()

def get_event_id(id_mapa, pos):
	event_file = open("./scripts/mapa/Mapa_" + str(id_mapa) + ".evt", "r")
	lines = event_file.readlines()

	for line in lines:
		if hex(EVT_HISTORIA) in line:
			ret = line.strip()
			ret = ret.split(",")[1].strip()
			ret = ret.split("|")
			if int(ret[1]) == pos:
				return int(ret[0])
	return -1


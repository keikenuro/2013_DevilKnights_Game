from util import *

#--------------------------------------------------------------------------------------------------------------
#ARCHIVO GENERAL
def XML_OpenData(filename):
	return minidom.parse(filename)

#--------------------------------------------------------------------------------------------------------------
#PERSONAJES
def XML_GetNamesList(f):
        aux = []
        for nodo in f.getElementsByTagName("Personaje"):
                aux.append(nodo.getAttribute("id"))
        return aux        

def XML_GetLevel(f, fk_id):
        for nodo in f.getElementsByTagName("Personaje"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("Nivel")[0].getAttribute("value"))

def XML_GetExp(f, fk_id):
        for nodo in f.getElementsByTagName("Personaje"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("Exp")[0].getAttribute("value"))

def XML_GetHP(f, fk_id):
        for nodo in f.getElementsByTagName("Personaje"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("HP")[0].getAttribute("value"))

def XML_GetMP(f, fk_id):
        for nodo in f.getElementsByTagName("Personaje"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("MP")[0].getAttribute("value"))

def XML_GetAtkF(f, fk_id):
        for nodo in f.getElementsByTagName("Personaje"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("AtkF")[0].getAttribute("value"))

def XML_GetAtkM(f, fk_id):
        for nodo in f.getElementsByTagName("Personaje"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("AtkM")[0].getAttribute("value"))
                        
def XML_GetDefF(f, fk_id):
        for nodo in f.getElementsByTagName("Personaje"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("DefF")[0].getAttribute("value"))

def XML_GetDefM(f, fk_id):
        for nodo in f.getElementsByTagName("Personaje"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("DefM")[0].getAttribute("value"))

def XML_GetSpeed(f, fk_id):
        for nodo in f.getElementsByTagName("Personaje"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("Speed")[0].getAttribute("value"))

def XML_GetEquip(f, fk_id):
        aux_list = []
        for nodo in f.getElementsByTagName("Personaje"):
                if nodo.getAttribute("id") == fk_id:
                        aux_list.append(int(nodo.getElementsByTagName("Cabeza")[0].getAttribute("objeto_id")))
                        aux_list.append(int(nodo.getElementsByTagName("Cuerpo")[0].getAttribute("objeto_id")))
                        aux_list.append(int(nodo.getElementsByTagName("Arma")[0].getAttribute("objeto_id")))
                        aux_list.append(int(nodo.getElementsByTagName("Acce1")[0].getAttribute("objeto_id")))
                        aux_list.append(int(nodo.getElementsByTagName("Acce2")[0].getAttribute("objeto_id")))
                        return aux_list

def XML_GetSkills(f, fk_id):
        aux_list = []
        for nodo in f.getElementsByTagName("Personaje"):
                if nodo.getAttribute("id") == fk_id:
                        for n in range(len(nodo.getElementsByTagName("Skill"))):
                                aux_list.append(int(nodo.getElementsByTagName("Skill")[n].getAttribute("id")))
                        return aux_list

#--------------------------------------------------------------------------------------------------------------
#ITEMS
def XML_GetItemName(f, fk_id):
        for nodo in f.getElementsByTagName("Item"):
                if nodo.getAttribute("id") == hex(fk_id):
                        return nodo.getElementsByTagName("Nombre")[0].getAttribute("value")

def XML_GetItemDescription(f, fk_id):
        for nodo in f.getElementsByTagName("Item"):
                if nodo.getAttribute("id") == hex(fk_id):
                        return nodo.getElementsByTagName("Descripcion")[0].getAttribute("value")	

def XML_GetItemUseable(f, fk_id):
        for nodo in f.getElementsByTagName("Item"):
                if nodo.getAttribute("id") == hex(fk_id):
                        return bool(int(nodo.getElementsByTagName("Usable")[0].getAttribute("value")))

def XML_GetItemEquipable(f, fk_id):
        for nodo in f.getElementsByTagName("Item"):
                if nodo.getAttribute("id") == hex(fk_id):
                        return bool(int(nodo.getElementsByTagName("Equipable")[0].getAttribute("value")))

def XML_GetItemEffect(f, fk_id):
        for nodo in f.getElementsByTagName("Item"):
                if nodo.getAttribute("id") == hex(fk_id) and fk_id == ITM_POCION:
			return ["HP","+", 25]
                elif nodo.getAttribute("id") == hex(fk_id) and fk_id == ITM_ETER:
			return ["MP", "+", 25]
                elif nodo.getAttribute("id") == hex(fk_id) and fk_id == ITM_REVIVE:
			return ["HP", "%", 1]
                elif nodo.getAttribute("id") == hex(fk_id) and fk_id == ITM_GRANADA:
			return ["HP", "-", "100"]
#--------------------------------------------------------------------------------------------------------------
#ITEMS
def XML_Get_Equip(f, nombre):
        #TODO
        equips = []
        for nodo in f.getElementsByTagName("Personaje"):
                if nodo.getAttribute("id") == nombre:
                        equips.append(Casco(int(nodo.getElementsByTagName("Cabeza")[0].getAttribute("objeto_id"))))
                        equips.append(Pechera(int(nodo.getElementsByTagName("Cuerpo")[0].getAttribute("objeto_id"))))
                        equips.append(Arma(int(nodo.getElementsByTagName("Arma")[0].getAttribute("objeto_id"))))
                        equips.append(Accesorio(int(nodo.getElementsByTagName("Acce1")[0].getAttribute("objeto_id"))))
                        equips.append(Accesorio(int(nodo.getElementsByTagName("Acce2")[0].getAttribute("objeto_id"))))
                        equips.append(Bota(int(nodo.getElementsByTagName("Botas")[0].getAttribute("objeto_id"))))
        return equips
        
def XML_GetGold(f):
        return int(f.getElementsByTagName("Oro")[0].firstChild.data)

def XML_GetTime(f):
        return f.getElementsByTagName("Tiempo")[0].firstChild.data

#--------------------------------------------------------------------------------------------------------------
#MALOS
def XML_GetBadList(f):
        aux = []
        for nodo in f.getElementsByTagName("Malo"):
                aux.append(nodo.getAttribute("id"))
        return aux 

def XML_GetBadName(f, fk_id):
        for nodo in f.getElementsByTagName("Malo"):
                if nodo.getAttribute("id") == fk_id:
                        return str(nodo.getElementsByTagName("Nombre")[0].getAttribute("value"))

def XML_GetBadHP(f, fk_id):
        for nodo in f.getElementsByTagName("Malo"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("HP")[0].getAttribute("value"))

def XML_GetBadMP(f, fk_id):
        for nodo in f.getElementsByTagName("Malo"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("MP")[0].getAttribute("value"))

def XML_GetBadAtkF(f, fk_id):
        for nodo in f.getElementsByTagName("Malo"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("AtkF")[0].getAttribute("value"))

def XML_GetBadAtkM(f, fk_id):
        for nodo in f.getElementsByTagName("Malo"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("AtkM")[0].getAttribute("value"))
                        
def XML_GetBadDefF(f, fk_id):
        for nodo in f.getElementsByTagName("Malo"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("DefF")[0].getAttribute("value"))

def XML_GetBadDefM(f, fk_id):
        for nodo in f.getElementsByTagName("Malo"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("DefM")[0].getAttribute("value"))

def XML_GetBadSpeed(f, fk_id):
        for nodo in f.getElementsByTagName("Malo"):
                if nodo.getAttribute("id") == fk_id:
                        return int(nodo.getElementsByTagName("Speed")[0].getAttribute("value"))


#Dimensiones
DIMS = [960, 560]
#---------------------------------------------------------#
#Animacion
PARADO_FRENTE = 0x0
PARADO_IZQ = 0x1
PARADO_DER = 0x2
PARADO_ATRAS = 0x3

CAMINANDO_FRENTE_2 = 0x4
CAMINANDO_FRENTE_1 = 0x5

CAMINANDO_IZQ_2 = 0x6
CAMINANDO_IZQ_1 = 0x7

CAMINANDO_DER_2 = 0x8
CAMINANDO_DER_1 = 0x9
	
CAMINANDO_ATRAS_2 = 0xA
CAMINANDO_ATRAS_1 = 0xB
#---------------------------------------------------------#
#Resultados del Menu Principal
NUEVO_JUEGO = 0x11
CARGAR_JUEGO = 0x12
MENU_OPCIONES = 0x13
MENU_EXTRAS = 0x14
SALIR = 0x15
__ERROR_UNKNOW = 0x0
#---------------------------------------------------------#
#Eventos
#Tipos de eventos
EVT_INICIO = 0x0
EVT_BATALLA_SIMPLE = 0x1
EVT_BATALLA_SUB_BOSS = 0x2
EVT_BATALLA_BOSS = 0x3
EVT_OBJETO_ENCONTRADO = 0x11
EVT_PERSONA_ENCONTRADA = 0x12
EVT_OBJETO_SINUSO = 0x13
EVT_HISTORIA = 0x21
EVT_TELEPORT = 0x31
EVT_MUSICA = 0x33
EVT_GAME_OVER = 0xFF

#Forma de los eventos
EVT_RANDOM = 0xF
EVT_NOEVENT = 0xA
#---------------------------------------------------------#
#ID_PERSONAJES
#--Jugables
ID_NICK = (0xAA, "Nick Evans")
#---------------------------------------------------------#
#ID_ATAQUES
#ID general para un ataque fisico directo
ATK_FISICO = 00

#ID general para un ataque magico directo
ATK_MAGICO = 01
#---------------------------------------------------------#
#ID_OBJETOS
OBJ_SILLON_1 = 0xA1
OBJ_SILLA_1 = 0xA2
OBJ_MESA_1 = 0xA3
OBJ_ESCALERA_1= 0xA4
OBJ_PUERTA_1= 0xA5
OBJ_PUERTA_2= 0xA6
OBJ_ALFOMBRA_1=0xA7
OBJ_ALFOMBRA_2=0xA8
OBJ_ALFOMBRA_3=0xA9
OBJ_CAMA_1=0xAA
OBJ_CAMA_2=0xAB
OBJ_SILLA_2=0xAC
OBJ_VENTANA_1=0xAD
OBJ_MESITA_1=0xAE
OBJ_BIBLIOTECA_1=0xAF
OBJ_MESACOCINA_1=0xB1
OBJ_MESACOCINA_2=0xB2
OBJ_MESACOCINA_3=0xB3
OBJ_MUEBLECOCINA_1=0xB4
OBJ_MUEBLECOCINA_2=0xB5
OBJ_HORNO_1=0xB6
OBJ_HORNO_2=0xB7
OBJ_MESACOMEDOR=0xB8
OBJ_CUADRO1=0xB9
OBJ_CUADRO2=0xBA
OBJ_CUADRO3=0xBB
OBJ_CUADRO4=0xBC
OBJ_ESPEJO=0xBD
OBJ_TESORO1=0xBE
OBJ_TESORO2=0xBF
OBJ_PERSONA_ALICE=0xC1
OBJ_PERSONA_CLAIRE=0xC2
OBJ_PERSONA_ERIKA=0xC3
OBJ_PERSONA_JOSEPH=0xC4
OBJ_PERSONA_KAREN=0xC5
OBJ_PERSONA_LEON=0xC6
OBJ_PERSONA_MARGARET=0xC7
OBJ_PERSONA_MATT=0xC8
OBJ_PERSONA_ROGER=0xC9
OBJ_PERSONA_SAM=0xCA
OBJ_PERSONA_WILLIAM=0xCB
#=========================ITEM=============================
#---------------------------------------------------------#
#Item
ITM_POCION = 0x1
ITM_ETER = 0x2
ITM_REVIVE = 0x3
ITM_GRANADA = 0x4

#---------------------------------------------------------#
#Armas
ARM_GLOCK = 0x1
ARM_STRIKER = 0x2
ARM_QSLAYER = 0x3

#---------------------------------------------------------#
#Armaduras
BDY_PECHERA_CUERO = 0x1
BDT_PECHERA_BRONZE = 0x2

#---------------------------------------------------------#
#Accesorio
ACC_COLGANTE_ZAFIRO = 0x1
ACC_COLGANTE_RUBY = 0x2
ACC_COLGANTE_ESMERALDA = 0x3

#---------------------------------------------------------#
#Cascos
CAS_LIGERO = 0x1
CAS_PESADO = 0x2
CAS_GALERA = 0x3
CAS_GORRO_INVIERNO = 0x4

#---------------------------------------------------------#
#Claves
CLV_LIBRO_CUENTOS = 0x1
CLV_CINTA_MARGARET = 0x2

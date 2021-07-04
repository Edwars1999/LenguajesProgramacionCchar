import ply.yacc as yacc

from lexcomp import tokens

#---------------PUNTO DE PARTIDA DE LA APLICACIÓN------------
def p_sentencias(p):
    '''sentencias : inicializacion
                  | condicionales
                  | repeticiones
                  | selecciones'''
#-------------------------------------------------------------



#--------------------------------------------------TIPOS DE DATOS USADOS------------------------------------------------
def p_tipoDato(p):
    '''tipoDato : INT
                | DOUBLE
                | STRING
                | CHAR
                | BOOL'''

def p_boleano(p):
    '''boleano : TRUE
               | FALSE '''

def p_numero(p):
    '''numero : ENTERO
              | DECIMAL'''
#-----------------------------------------------------------------------------------------------------------------------








#----------------------------------------------INICIALIZACION: Edwars Sabando-------------------------------------------
def p_inicializacion(p):
    '''inicializacion : declaracion
                      | asignacion'''

#-----------------------DECLARACION DE VARIABLES------------------------
def p_declaracion(p):
    '''declaracion : declaracionEntero
                   | declaracionFlotante
                   | declaracionCadena
                   | declaracionCaracter
                   | declaracionBooleano
                   | declaracionEstructura'''

def p_declaracionEntero(p):
    '''declaracionEntero : INT VARIABLE ASIGNACION ENTERO FINSENTENCIA
                         | INT VARIABLE FINSENTENCIA
                         | INT VARIABLE ASIGNACION operacionesNumero FINSENTENCIA'''

def p_declaracionFlotante(p):
    '''declaracionFlotante : DOUBLE VARIABLE ASIGNACION DECIMAL FINSENTENCIA
                           | DOUBLE VARIABLE FINSENTENCIA
                           | DOUBLE VARIABLE ASIGNACION operacionesNumero FINSENTENCIA'''

def p_declaracionCadena(p):
    '''declaracionCadena : STRING VARIABLE ASIGNACION CADENA FINSENTENCIA
                         | STRING VARIABLE FINSENTENCIA
                         | STRING VARIABLE ASIGNACION operacionesCadena FINSENTENCIA'''

def p_declaracionCaracter(p):
    '''declaracionCaracter : CHAR VARIABLE ASIGNACION CARACTER FINSENTENCIA
                           | CHAR VARIABLE FINSENTENCIA'''

def p_declaracionBooleano(p):
    '''declaracionBooleano : BOOL VARIABLE ASIGNACION boleano FINSENTENCIA
                           | BOOL VARIABLE FINSENTENCIA'''

def p_declaracionEstructura(p):
    '''declaracionEstructura : diccionario
                             | lista
                             | pila'''
#----------------------------------------------------------------------
#-----------------------ASIGNACION DE VARIABLES------------------------
def p_asignacion(p):
    '''asignacion : VARIABLE ASIGNACION VARIABLE FINSENTENCIA
                  | VARIABLE ASIGNACION CADENA FINSENTENCIA
                  | VARIABLE ASIGNACION CARACTER FINSENTENCIA
                  | VARIABLE ASIGNACION numero FINSENTENCIA
                  | VARIABLE ASIGNACION boleano FINSENTENCIA
                  | VARIABLE ASIGNACION operacionesNumero FINSENTENCIA
                  | VARIABLE ASIGNACION operacionesCadena FINSENTENCIA'''

def p_operacionesNumero(p):
    '''operacionesNumero : expresion repOp
                         | expresion '''

def p_operacionesCadena(p):
    '''operacionesCadena : CADENA
                         | CADENA SUMA operacionesCadena'''

def p_expresion(p):
    '''expresion : numero
                 | VARIABLE
                 | PARENSTART operacionesNumero PARENEND
                 | PARENSTART VARIABLE PARENEND
                 | PARENSTART numero PARENEND'''

def p_repOp(p):
    '''repOp : operador expresion
             | operador expresion repOp'''

def p_operador(p):
    '''operador : SUMA
                | RESTA
                | MULTIPLICA
                | DIVISION
                | MODULO '''
#----------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------








#--------------------------------------------------ESTRUCTURAS DE CONTROL-----------------------------------------------
def p_selecciones(p):
    '''selecciones : opSWITCH'''


def p_opSwitch(p):
    'opSWITCH : SWITCH PARENSTART VARIABLE PARENEND LLAVESTART cases DEFAULT DOSPUNTOS sentencias BREAK FINSENTENCIA LLAVEEND'


def p_cases(p):
    '''cases : CASE VARIABLE DOSPUNTOS sentencias BREAK FINSENTENCIA
             | CASE VARIABLE DOSPUNTOS sentencias BREAK FINSENTENCIA cases
             | CASE numero DOSPUNTOS sentencias BREAK FINSENTENCIA
             | CASE numero DOSPUNTOS sentencias BREAK FINSENTENCIA cases
             | CASE CADENA DOSPUNTOS sentencias BREAK FINSENTENCIA
             | CASE CADENA DOSPUNTOS sentencias BREAK FINSENTENCIA cases'''


def p_repeticiones(p):
    '''repeticiones : opWHILE'''


def p_opWhile(p):
    '''opWHILE : WHILE  PARENSTART condicion PARENEND LLAVESTART  LLAVEEND
               | WHILE  PARENSTART condicion PARENEND LLAVESTART  sentencias LLAVEEND '''


def p_condicionales(p):
    '''condicionales : opIF'''


def p_opIf(p): 
    '''opIF : IF  PARENSTART condicion PARENEND LLAVESTART LLAVEEND
            | IF  PARENSTART condicion PARENEND LLAVESTART LLAVEEND ELSE opIF
            | IF  PARENSTART condicion PARENEND LLAVESTART LLAVEEND ELSE LLAVESTART LLAVEEND
            | IF  PARENSTART condicion PARENEND LLAVESTART sentencias LLAVEEND
            | IF  PARENSTART condicion PARENEND LLAVESTART sentencias LLAVEEND ELSE opIF
            | IF  PARENSTART condicion PARENEND LLAVESTART sentencias LLAVEEND ELSE LLAVESTART LLAVEEND '''


def p_condicion(p):
    '''condicion : numero exComparadora numero
                 | numero exComparadora VARIABLE
                 | VARIABLE exComparadora VARIABLE
                 | VARIABLE exComparadora numero
                 | PARENSTART condicion PARENEND adicionCondicion condicion
                 | PARENSTART condicion PARENEND
                 | boleano
                 | VARIABLE
                 | NEGACION boleano
                 | NEGACION VARIABLE'''


def p_exComparadora(p):
    '''exComparadora : MAYORQUE
                     | MENORQUE
                     | MAYORIGUAL
                     | MENORIGUAL
                     | IGUALDAD
                     | DESIGUALDAD'''

def p_adicionCondicion(p):
    '''adicionCondicion : AND
                        | OR'''
#-----------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------ESTRUCTURAS DE DATOS-------------------------------------------------
def p_pila(p):
    '''pila : STACK MENORQUE valor MAYORQUE VARIABLE ASIGNACION NEW STACK MENORQUE valor MAYORQUE PARENSTART PARENEND FINSENTENCIA
            | STACK MENORQUE valor MAYORQUE VARIABLE FINSENTENCIA
            | VARIABLE ASIGNACION NEW STACK MENORQUE valor MAYORQUE PARENSTART PARENEND FINSENTENCIA
            | metodosPila'''


def p_metodosPila(p):
    '''metodosPila : VARIABLE PUNTO PEEK PARENSTART PARENEND FINSENTENCIA
                    | VARIABLE PUNTO POP PARENSTART PARENEND FINSENTENCIA
                    | metodoClear'''


def p_lista(p):
    '''lista : LIST MENORQUE valor MAYORQUE VARIABLE ASIGNACION NEW LIST MENORQUE valor MAYORQUE PARENSTART PARENEND FINSENTENCIA
             | LIST MENORQUE valor MAYORQUE VARIABLE FINSENTENCIA
             | VARIABLE ASIGNACION NEW LIST MENORQUE valor MAYORQUE PARENSTART PARENEND FINSENTENCIA
             | metodosLista'''


def p_metodosLista(p):
    '''metodosLista : VARIABLE PUNTO ADD PARENSTART valorEstructuras PARENEND FINSENTENCIA
                    | VARIABLE PUNTO REMOVE PARENSTART PARENEND FINSENTENCIA
                    | metodoClear'''


def p_diccionario(p):
    '''diccionario : DICTIONARY MENORQUE clave COMA valor MAYORQUE VARIABLE ASIGNACION NEW DICTIONARY MENORQUE clave COMA valor MAYORQUE PARENSTART PARENEND FINSENTENCIA
                   | DICTIONARY MENORQUE clave COMA valor MAYORQUE VARIABLE FINSENTENCIA
                   | VARIABLE ASIGNACION NEW DICTIONARY MENORQUE clave COMA valor MAYORQUE PARENSTART PARENEND FINSENTENCIA
                   | metodosDic'''


def p_metodosDic(p):
    '''metodosDic : VARIABLE PUNTO ADD PARENSTART COMA valorEstructuras PARENEND FINSENTENCIA
                  | VARIABLE PUNTO CONTAINSKEY PARENSTART PARENEND FINSENTENCIA
                  | metodoClear'''


def p_metodoClear(p):
    'metodoClear : VARIABLE PUNTO CLEAR PARENSTART PARENEND FINSENTENCIA'


def p_valorEstructuras(p):
    '''valorEstructuras : VARIABLE
                        | numero
                        | CADENA
                        | NEW estructura'''

def p_clave(p):
    '''clave : INT
             | DOUBLE
             | STRING
             | CHAR'''


def p_valor(p):
    '''valor : tipoDato
             | estructura'''


def p_estructura(p):
    '''estructura :  DICTIONARY MENORQUE clave COMA valor MAYORQUE 
                  |  LIST MENORQUE valor MAYORQUE
                  |  STACK MENORQUE valor MENORQUE  '''

#-----------------------------------------------------------------------------------------------------------------------

# Manejo de errores
def p_error(p):
    print("Su sentencia no es aceptada por C#!")



# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('Probar sentido > ')
    except EOFError:
       break
    if not s: continue
    result = parser.parse(s)
    print(result)

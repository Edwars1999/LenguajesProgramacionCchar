# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

from lexcomp import tokens
 ###----AQUI COMIENZA EL TRABAJO DE JORGE----###
def p_sentencias(p):### se agrega las instrucciones del programa
    '''sentencias : condicionales
                  | repeticiones
                  | inicializacion '''


# -- Trabajo de Edwars: Ciclo While y Estructura Listas
def p_repeticiones(p):
    '''repeticiones: opWHILE'''

def p_opWhile(p):
    '''opWHILE : WHILE  PARENSTART condicion PARENEND LLAVESTART  LLAVEEND
               | WHILE  PARENSTART condicion PARENEND LLAVESTART  sentencias LLAVEEND '''
# -- Fin de trabajo hecho por Edwars --

def p_condicionales(p):
    '''condicionales : opIF'''

def p_opIf(p): 
    '''opIF : IF  PARENSTART condicion PARENEND LLAVESTART  LLAVEEND
            | IF  PARENSTART condicion PARENEND LLAVESTART  LLAVEEND ELSE opIF
            | IF  PARENSTART condicion PARENEND LLAVESTART  LLAVEEND ELSE LLAVESTART  LLAVEEND
            | IF  PARENSTART condicion PARENEND LLAVESTART  sentencias LLAVEEND
            | IF  PARENSTART condicion PARENEND LLAVESTART  sentencias LLAVEEND ELSE opIF
            | IF  PARENSTART condicion PARENEND LLAVESTART  sentencias LLAVEEND ELSE LLAVESTART  LLAVEEND '''

def p_condicion(p):
    '''condicion : dato exComparadora dato
                 | dato exComparadora condicion
                 | PARENSTART condicion PARENEND exComparadora  condicion 
                 | PARENSTART condicion PARENEND
                 | boleano
                 | NEGACION boleano
                 | NEGACION VARIABLE
                 | VARIABLE'''

def p_exComparadora(p):
    '''exComparadora : AND
                     | OR
                     | MAYORQUE
                     | MENORQUE
                     | MAYORIGUAL
                     | MENORIGUAL
                     | IGUALDAD
                     | DESIGUALDAD'''

def p_inicializacion(p):
    '''inicializacion : declaracion
                      | asignacion'''

def p_declaracion(p):
    '''declaracion : tipoDato VARIABLE ASIGNACION dato FINSENTENCIA
                   | tipoDato VARIABLE FINSENTENCIA
                   | tipoDato VARIABLE ASIGNACION operaciones FINSENTENCIA
                   | decEstructura'''

def p_decEstructura(p):
    '''decEstructura : diccionario'''

def p_diccionario(p):
    '''diccionario : DICTIONARY MENORQUE clave COMA valor MAYORQUE VARIABLE ASIGNACION NEW DICTIONARY MENORQUE clave COMA valor MAYORQUE PARENSTART PARENEND FINSENTENCIA
                   | DICTIONARY MENORQUE clave COMA valor MAYORQUE VARIABLE FINSENTENCIA
                   | VARIABLE IGUALDAD NEW DICTIONARY MENORQUE clave COMA valor MAYORQUE PARENSTART PARENEND FINSENTENCIA
                   | metodosDic'''

def p_metodosDic(p):
    '''metodosDic : VARIABLE PUNTO ADD PARENSTART dato COMA valorMetDic PARENEND FINSENTENCIA'''

def p_valorMetDic(p):
    '''valorMetDic : dato
                   | NEW estructura'''

def p_clave(p):
    '''clave : INT
                | FLOAT
                | DOUBLE
                | STRING
                | LONG
                | CHAR
                | SHORT
                | BYTE
                | SBYTE
                | UINT
                | USHORT
                | ULONG'''

def p_valor(p):
    '''valor : tipoDato
             | estructura'''

def p_estructura(p):
    '''estructura :  DICTIONARY MENORQUE clave COMA valor MAYORQUE 
                  |  LIST MENORQUE valor MAYORQUE
                  |  STACK MENORQUE valor MENORQUE  '''

def p_asignacion(p):
    '''asignacion : VARIABLE ASIGNACION dato FINSENTENCIA
                  | VARIABLE ASIGNACION boleano FINSENTENCIA
                  | VARIABLE ASIGNACION operaciones FINSENTENCIA'''

def p_dato(p):
    '''dato : VARIABLE 
            | numero
            | CADENA '''

def p_tipoDato(p):
    '''tipoDato : INT
                | FLOAT
                | DOUBLE
                | STRING
                | LONG
                | CHAR
                | SHORT
                | BYTE
                | SBYTE
                | UINT
                | USHORT
                | ULONG
                | BOOL'''

            
def p_boleano(p):
    '''boleano : TRUE
                | FALSE '''

def p_numero(p):
    '''numero : ENTERO
             | DECIMAL'''

def p_operaciones(p):
    '''operaciones :  expresion repOp 
                   | expresion '''

def p_repOpe(p):
    '''repOp : operador expresion 
            | operador expresion repOp'''

def p_expresion(p):
    '''expresion : numero
                 | VARIABLE
                 | PARENSTART  operaciones PARENEND
                 | PARENSTART  VARIABLE PARENEND
                 | PARENSTART  numero PARENEND'''

def p_operador(p):
    '''operador : SUMA
                | RESTA
                | MULTIPLICA
                | DIVISION
                | MODULO ''' 
 ###----AQUI TERMINA EL TRABAJO DEL PROFE----#

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
       break
    if not s: continue
    result = parser.parse(s)
    print(result)

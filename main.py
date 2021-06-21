# ------------------------------------------------------------
# Tokenizer para comparar palabras, numeros y valores de verdad
# ------------------------------------------------------------
import ply.lex as lex

# --------- Comienzo de Trabajo por: Edwars Sabando --------

# Lista de tokens
tokens = [
    'VALORVERDAD',
    'VARIABLE',
    'NUMERO',
    'IGUALDAD',
    'ASIGNACION', #JORGE
    'DESIGUALDAD',
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'FINSENTENCIA',
    #----JORGE PITA AGREGÓ ESTO----
    'CADENA',
    'AGRUPASTART',
    'AGRUPAEND',
    'LLAVESTART',
    'LLAVEEND'
]


# Reglas de expresiones regulares para tokens simples
t_VALORVERDAD   = r'(true|false)'
t_VARIABLE      = r'^[a-zA-Z]\w*'
t_NUMERO        = r'-?\d+(.\d+)?'
t_IGUALDAD      = r'=='
t_DESIGUALDAD   = r'!='
t_ASIGNACION    = r'\='
t_MAYORIGUAL    = r'>='
t_MENORIGUAL    = r'<='
t_MAYORQUE      = r'>'
t_MENORQUE      = r'<'
t_FINSENTENCIA  = r';'
t_CADENA        = r'\".*\"$' #JORGE AGREGÓ ESTA EXPRESION REGULAR
t_AGRUPASTART   = r'\('
t_AGRUPAEND     = r'\)'
t_LLAVESTART    = r'\{'
t_LLAVEEND      = r'\}'


# --------- Fin de Trabajo por: Edwars Sabando --------

# --------- Comienzo de trabajo de Jorge ------------#
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'string' : 'STRING',
    'int' : 'INT',
    'switch' : 'SWITCH',
    'double' : 'DOUBLE',
    'float' : 'FLOAT',

# --------- Comienzo de trabajo de Luis ------------#
    'break': 'BREAK',
    'bool': 'BOOL',
    'byte': 'BYTE',
    'case': 'CASE',
    'char': 'CHAR',
    'continue': 'CONTINUE',
    'default': 'DEFAULT',
    'do': 'DO',
    'for': 'FOR',
    'foreach': 'FOREACH',
    'in': 'IN',
    'long': 'LONG',
    'new': 'NEW',
    'null': 'NULL',
    'return': 'RETURN',
    'sbyte': 'SBYTE',
    'short': 'SHORT',
    'this': 'THIS',
    'uint': 'UINT',
    'ulong': 'ULONG',
    'ushort': 'USHORT'
# ----------- FIN DE TRABAJO DE LUIS------#
}

tokens = tokens + list(reserved.values())

def t_ID(t):
     r'[a-zA-Z_]\w*'
     t.type = reserved.get(t.value,'VARIABLE')    # Check for reserved words
     return t
# ----------- FIN DE TRABAJO DE JORGE------#

# Regla para seguir los números de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Permite ignorar si en la cadena existen espacios vacíos o tabulaciones
t_ignore = ' \t'


# Regla de manejo de errores
def t_error(t):
    print("Elemento no válido: '%s'" % t.value[0])
    t.lexer.skip(1)


# Completar el lexer luego de definir las reglas
lexer = lex.lex()


# -------------------------------- SECCIÓN DEDICADA A PRUEBAS -------------------------------------

# Compara con las tokens
def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No existen más entradas
        print(tok)

line = " "

while line != "" :
    line = input(">>")
    lexer.input(line);
    getTokens(lexer)

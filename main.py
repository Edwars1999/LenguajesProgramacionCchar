# ------------------------------------------------------------
# Tokenizer para comparar palabras, numeros y valores de verdad
# ------------------------------------------------------------
import ply.lex as lex

# --------- Comienzo de Trabajo por: Edwars Sabando --------

# Lista de tokens
tokens = [
    #'DOBLECOMILLA',
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
    #----JORGE PITA AGREGO ESTO--##
    'PUNTOYCOMA',
    'CADENA',
    'AGRUPACION'
]


# Reglas de expresiones regulares para tokens simples
#t_DOBLECOMILLA  = r'\"'
t_VALORVERDAD   = r'((T|t)rue|(F|f)alse)'
#t_ID            = r'[a-zA-Z_]\w*'
t_NUMERO        = r'-?\d+(.\d+)?'
t_IGUALDAD      = r'=='
t_DESIGUALDAD   = r'!='
t_ASIGNACION    = r'\='
t_MAYORIGUAL    = r'>='
t_MENORIGUAL    = r'<='
t_MAYORQUE      = r'>'
t_MENORQUE      = r'<'
t_FINSENTENCIA  = r';'
t_PUNTOYCOMA    = r'\;' #JORGE PITA
t_CADENA        = r'\".*\"$' #JORGE AGREGO ESTA EXPRESION REGULAR
t_AGRUPACION    = r'[\(\)]'


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
    'float' : 'FLOAT'
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


# La librería lex recibe la información a evaluar
#lexer.input(datos)

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


# ------------------------------------------------------------
# Tokenizer para comparar palabras, numeros y valores de verdad
# ------------------------------------------------------------
import ply.lex as lex

# Lista de tokens
tokens = [
    'VARIABLE',
    'ENTERO',
    'DECIMAL',
    'IGUALDAD',
    'DESIGUALDAD',
    'ASIGNACION',
    'MAYORIGUAL',
    'MENORIGUAL',
    'MAYORQUE',
    'MENORQUE',
    'FINSENTENCIA',
    'CADENA',
    'CARACTER',
    'LLAVESTART',
    'LLAVEEND',
    'PARENSTART',
    'PARENEND',
    'SUMA',
    'RESTA',
    'MULTIPLICA',
    'DIVISION',
    'MODULO',
    'AND',
    'OR',
    'NEGACION',
    'COMA',
    'SPACE',
    'PUNTO',
    'DOSPUNTOS'
]


# Reglas de expresiones regulares para tokens simples
t_ENTERO        = r'\-?\d+'
t_DECIMAL       = r'\-?\d+\.\d+'
t_IGUALDAD      = r'=='
t_DESIGUALDAD   = r'!='
t_ASIGNACION    = r'='
t_MAYORIGUAL    = r'>='
t_MENORIGUAL    = r'<='
t_MAYORQUE      = r'>'
t_MENORQUE      = r'<'
t_DOSPUNTOS     = r':'
t_FINSENTENCIA  = r';'
t_CADENA        = r'".*"'
t_CARACTER      = r'\'.\''
t_LLAVESTART    = r'\{'
t_LLAVEEND      = r'\}'
t_PARENSTART    = r'\('
t_PARENEND      = r'\)'
t_SUMA          = r'\+'
t_RESTA         = r'\-'
t_MULTIPLICA    = r'\*'
t_DIVISION      = r'\/'
t_MODULO        = r'\%'
t_AND           = r'&&'
t_OR            = r'\|\|'
t_NEGACION      = r'\!'
t_COMA          = r'\,'
t_SPACE         = r'\s+'
t_PUNTO         = r'\.'


reserved = {
    'add'           : 'ADD',
    'clear'         : 'CLEAR',
    'peek'          : 'PEEK',
    'pop'           : 'POP',
    'remove'        : 'REMOVE',
    'ContainsKey'   : 'CONTAINSKEY',
    'List'          : 'LIST',
    'Stack'         : 'STACK',
    'Dictionary'    : 'DICTIONARY',
    'if'            : 'IF',
    'else'          : 'ELSE',
    'while'         : 'WHILE',
    'string'        : 'STRING',
    'int'           : 'INT',
    'switch'        : 'SWITCH',
    'double'        : 'DOUBLE',
    'true'          : 'TRUE',
    'false'         : 'FALSE',
    'break'         : 'BREAK',
    'bool'          : 'BOOL',
    'case'          : 'CASE',
    'char'          : 'CHAR',
    'continue'      : 'CONTINUE',
    'const'         : 'CONST',
    'default'       : 'DEFAULT',
    'in'            : 'IN',
    'new'           : 'NEW',
    'null'          : 'NULL',
    'return'        : 'RETURN',
    'this'          : 'THIS',
    'public'        : 'PUBLIC',
    'private'       : 'PRIVATE',
    'protected'     : 'PROTECTED',
    'void'          : 'VOID',
    'static'        : 'STATIC',
    'async'         : 'ASYNC',
    'unsafe'        : 'UNSAFE',
    'extern'        : 'EXTERN'
}

tokens = tokens + list(reserved.values())

def t_VARIABLE(t):
     r'^[a-zA-Z_]\w*$'
     t.type = reserved.get(t.value, 'VARIABLE')    # Check for reserved words
     return t

# Regla para seguir los números de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Permite ignorar si en la cadena existen espacios vacíos o tabulaciones
t_ignore = ' \t\n'


# Permite pasar los comentarios
def t_COMMENT(t):
    r'(^//.*$|^///.*$|^/\*.*\*/$)'
    pass


# Regla de manejo de errores
def t_error(t):
    print("Elemento no válido: '%s'" % t.value[0])
    global aux
    aux = "Elemento no válido: '%s'" % t.value[0]
    t.lexer.skip(1)


# Completar el lexer luego de definir las reglas
lexer = lex.lex()


# -------------------------------- SECCIÓN DEDICADA A PRUEBAS -------------------------------------

# Compara con las tokens
def getTokens(lexer):
    variable = ''
    global aux
    aux = ''
    while True:
        tok = lexer.token()
        if not tok:
            break  # No existen más entradas
        print(tok)
        if(len(aux)!=0):
            variable += aux + '\n'
        variable += str(tok) + '\n'
    return variable

line = " "


#-----------------------------------ALGORITMO DE PRUEBA: COMPONENTE LÉXICO----------------------------------------------

#Prueba con archivo
'''
archivo = open("pruebaLexico.txt")
for linea in archivo:
    print(">>" + linea)
    lexer.input(linea)
    getTokens(lexer)
    if len(linea) == 0:
        break
'''

#Prueba Interfaz
def pruebaInt(codigo):
    txt = codigo.split('\n')
    variable = ''
    for linea in txt:
        print(">>" + linea)
        lexer.input(linea)
        variable += '>>' + linea + '\n'
        variable += getTokens(lexer)
        #if len(linea) == 0:
         #   break
    return variable



#Prueba en consola
"""while line != "" :
   line = input(">>")
   lexer.input(line);
   getTokens(lexer)
"""

#-----------------------------------------------------------------------------------------------------------------------
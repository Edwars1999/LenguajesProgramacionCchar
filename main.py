# ------------------------------------------------------------
# Tokenizer para comparar palabras, numeros y valores de verdad
# ------------------------------------------------------------
import ply.lex as lex

# --------- Comienzo de Trabajo por: Edwars Sabando --------

# Lista de tokens
tokens = (
    'DOBLECOMILLA',
    'VALORVERDAD',
    'ID',
    'NUMERO',
    'IGUALDAD',
    'DESIGUALDAD',
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'FINSENTENCIA'
)


# Reglas de expresiones regulares para tokens simples
t_DOBLECOMILLA  = r'\"'
t_VALORVERDAD   = r'((T|t)rue|(F|f)alse)'
t_ID            = r'[a-zA-Z]\w*'
t_NUMERO        = r'-?\d+(.\d+)?'
t_IGUALDAD      = r'=='
t_DESIGUALDAD   = r'!='
t_MAYORIGUAL    = r'>='
t_MENORIGUAL    = r'<='
t_MAYORQUE      = r'>'
t_MENORQUE      = r'<'
t_FINSENTENCIA  = r';'

# --------- Fin de Trabajo por: Edwars Sabando --------

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
datos = '''
 3 >= false;
 True == Genial;
 Truebolic = ironico;
 -3.02 != False;
 assd <= true;
 -40 > 0.2
 falselogic < asdas
 '''

# La librería lex recibe la información a evaluar
lexer.input(datos)

# Compara con las tokens
while True:
    tok = lexer.token()
    if not tok:
        break  # No existen más entradas
    print(tok)
# De entrada

# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'COMILLA',
    'NUMERO',
    'CARACTERES', 
    'LLAVEAB',
    'LLAVECE', 
    'INTERPOLACION',
    'MAS',
    'VARIABLE',
    'PUNTOCOMA'
)

# Regular expression rules for simple tokens
t_COMILLA = r'\"'
t_NUMERO = r'-?\d+(\.\d+)?'
t_CARACTERES = r'[\w]+'
t_LLAVEAB = r'\{'
t_LLAVECE= r'\}'
t_INTERPOLACION = r'\$'
t_MAS = r'\+'
t_VARIABLE = r'\[a-zA-Z]+\w*'
t_PUNTOCOMA = r'\;'


# A regular expression rule with some action code



# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
 3 + 4 * 10
   + -20 *2
 '''

# Give the lexer some input

#lexer.input(data)

# Tokenize
def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

linea =  " "

while linea!="":
    linea = input(">>")
    lexer.input(linea)
    getTokens(lexer)

print("Susscesfull")
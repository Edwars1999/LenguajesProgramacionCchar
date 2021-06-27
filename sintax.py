# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

from lexcomp import tokens
 

def p_inicializacion(p):
    '''inicializacion : declaracion
                      | asignacion
                      | operaciones'''

def p_declaracion(p):
    '''declaracion : tipoDato VARIABLE ASIGNACION dato FINSENTENCIA
                   | tipoDato VARIABLE FINSENTENCIA
                   | tipoDato VARIABLE ASIGNACION operaciones FINSENTENCIA'''

def p_asignacion(p):
    '''asignacion : VARIABLE ASIGNACION dato FINSENTENCIA
                  | VARIABLE ASIGNACION operaciones FINSENTENCIA'''

def p_dato(p):
    '''dato : VARIABLE 
            | numero
            | CADENA 
            | boleano'''

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
                | ULONG'''
            
def p_boleano(p):
    '''boleano : TRUE
                | FALSE '''

def p_numero(p):
    '''numero : ENTERO
             | DECIMAL'''

def p_operaciones(p):
    'operaciones :  expresion repOp '

def p_repOpe(p):
    '''repOp : operador expresion 
            | operador expresion repOp'''

def p_expresion(p):
    '''expresion : numero
                 | VARIABLE
                 | PARENSTART  operaciones PARENEND'''

def p_operador(p):
    '''operador : SUMA
                | RESTA
                | MULTIPLICA
                | DIVISION
                | MODULO ''' 

'''def p_expression_suma(p):
    'expression : expression SUMA term'
    p[0] = p[1] + p[3]


def p_expression_resta(p):
    'expression : expression RESTA term'
    p[0] = p[1] - p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_mult(p):
    'term : term MULTIPLICA factor'
    p[0] = p[1] * p[3]


def p_term_division(p):
    'term : term DIVISION factor'
    p[0] = p[1] / p[3]


def p_term_modulo(p):
    'term : term MODULO factor'
    p[0] = p[1] % p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_entero(p):
    'factor : ENTERO'
    p[0] = p[1]

def p_factor_decimal(p):
    'factor : DECIMAL'
    p[0] = p[1]


def p_factor_expr(p):
    'factor : PARENSTART expression PARENEND'
    p[0] = p[2]

'''
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

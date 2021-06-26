# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

from lexcomp import tokens

def p_expression_suma(p):
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


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

#while True:
#    try:
#        s = raw_input('calc > ')
#    except EOFError:
 #       break
  #  if not s: continue
   # result = parser.parse(s)
   # print(result)

import sys
if ".." not in sys.path: sys.path.insert(0,"..")

import ply.lex as lex

from ply.lex import TOKEN

tokens = [
    # Test String Rules
    "TIMES", "POWER",       # Should parse (TIMES, TIMES)
    "TRUNCATE", "DIVIDE",   # Should parse (TRUNCATE | DIVIDE)
    "BITOR", "OR",          # Should parse (BITOR, BITOR)
    "AND", "BITAND",        # Should parse (AND | BITAND)

    # Test Function Rules
    "PLUS", "INC",          # Should parse (PLUS, PLUS)
    "DEC",  "MINUS",        # Should parse (DEC | MINUS)
    "ASSIGN", "EQ",         # Should parse (ASSIGN, ASSIGN)
    "NAMESPACE", "ASTYPE",  # Should parse (NAMESPACE | ASTYPE)
 ]

# Tokens '*' before '**', should preserve.
t_TIMES     = r'\*'
t_POWER     = r'\*\*'

# Tokens '/' before '//', should reverse.
t_DIVIDE    = r'/'
t_TRUNCATE  = r'//'

# Tokens '||' before '|', should reverse.
t_OR        = r'\|\|'
t_BITOR     = r'\|'

# Tokens '&&' before '&', should preserve.
t_AND       = r'\&\&'
t_BITAND    = r'\&'


# Tokens '+' before '++', should preserve.
@TOKEN(r'\+')
def t_PLUS(t):
    return t


@TOKEN(r'\+\+')
def t_INC(t):
    return t


# Tokens '-' before '--', should reverse.
@TOKEN(r'\-')
def t_MINUS(t):
    return t


@TOKEN(r'\-\-')
def t_DEC(t):
    return t


# Tokens '==' before '=', should reverse.
@TOKEN(r'\=\=')
def t_EQ(t):
    return t


@TOKEN(r'\=')
def t_ASSIGN(t):
    return t


# Tokens '::' before ':', should preserve
@TOKEN(r'::')
def t_NAMESPACE(t):
    return t


@TOKEN(r':')
def t_ASTYPE(t):
    return t


t_ignore = r' '


def t_error(t):
    pass


if __name__ == '__main__':
    lexer = lex.lex(ordered=True, debug=True)

    lexer.input(sys.argv[1])
    for token in lexer.tokens():
        if hasattr(token, 'lexer'):
            l = token.lexer
            print token, l.lexpos, l.lexstate
        else:
            print token, 'DONE'

else:
    lex.lex(ordered=True)
    lex.runmain(data='* / | & ** // || && + - = : ++ -- == ::')

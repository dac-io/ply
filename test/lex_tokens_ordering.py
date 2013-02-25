import sys
if ".." not in sys.path: sys.path.insert(0,"..")

import ply.lex as lex

from ply.lex import TOKEN

tokens = [
    "PLUS", "INC",          # Should parse (PLUS, PLUS)
    "DEC",  "MINUS",        # Should parse (DEC | MINUS)
    "ASSIGN", "EQ",         # Should parse (ASSIGN, ASSIGN)
    "DECLARE", "ASTYPE",    # Should parse (DECLARE | ASTYPE)
    ]


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


# Tokens ':=' before ':', should preserve
@TOKEN(r':=')
def t_DECLARE(t):
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
    while True:
        token = lexer.token()
        if token is not None:
            if hasattr(token, 'lexer'):
                l = token.lexer
                print token, l.lexpos, l.lexstate
            else:
                print token, 'DONE'
        else:
            break

else:
    lex.lex(ordered=True)
    lex.runmain(data='+ - = : ++ -- == :=')

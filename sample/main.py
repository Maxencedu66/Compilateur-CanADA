import grammaire as g
from AST import Node
from analyseurLexical import analyseurLexical, Token
from sys import argv

filename = "../data/test1_correct.ada"
if len(argv) > 1:
    filename = argv[1]

g.VERBOSE = False

tokens: list[Token]
lexique: list[str]
tokens, lexique = analyseurLexical(argv[1] if len(argv)>=2 else "../data/test1_correct.ada")

if Token.has_lexical_error:
    exit(2)

g.analyse(tokens, lexique)
g.end(0)
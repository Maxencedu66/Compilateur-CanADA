import re
from token_pcl import Token, MAX_IDENT_SIZE, MAX_CONST_SIZE, CONST_CODE, STR_CODE, codes, keywords, operators
from os.path import isfile as os_isfile
from sys import stderr

def analyseurLexical(nomFichier:str = "../data/test1_correct.ada") -> (list[Token],list[str]):
    """
    Return une liste des Tokens luent dans un fichier
    """
    tokens = []
    stack = ""
    stash = ""
    automate = None
    lexique = []
    def tok_append(id_line:int=None)->None:
        nonlocal stack  # Tell the function to use the variable defined in the parent scope
        if not stack:
            return
        if re.match("^[a-zA-Z]([a-zA-Z0-9_])*$", stack) and len(stack) <= MAX_IDENT_SIZE and stack not in keywords:
# Si stack contient un ident, on rentre ce dernier dans la table des symboles et on crée le token de la façon suivante : 
# Token("ident", id_line, indice de l'ident dans la table des symboles)
# On reconnaît un ident ssi il correspond au regex, qu'il n'est pas trop long et qu'il n'est ni dans les mots clés, ni dans les symboles déjà reconnus
# ATTENTION : Les keywords sont entre 0 et 99, les opérateurs enrte 100 et 199, les symboles auront pour code 300 et plus !!!
            for i in range(len(lexique)):
                if lexique[i]==stack:   # Si on trouve dans lexique on ajoute le code dans tokens
                    tokens.append(Token(lexique[i], id_line, i+300))
                    stack = ""
                    return  # Sort de la fonction
            lexique.append(stack)   # Sinon on ajoute stack dans le lexique
            tokens.append(Token(lexique[-1], id_line, len(lexique)+299)) # len(lexique) + 300 - 1 car # car stack est le dernier elt de lexique
            stack = ""
            return  # Sort de la fonction   
        tokens.append(Token(stack, id_line))    # Si pas IDENT
        stack = ""
    def zero(c:str, id_line:int=None)->None:
        nonlocal stack
        nonlocal stash
        nonlocal automate
        # print(f"0: '{c}'\t'{stack}'\t'{stash}'")
        if c in [op[0] for op in operators]:
            stash = stack
            tok_append(id_line)
            stack = c
            automate = one
            return
        if c in [' ', '\t', '\n']:
            tok_append(id_line)
            return
        if c == '"': # Si on reconnaît le début d'une chaîne de caractères, on va à l'état 2 de l'automate
            stack += c
            automate = two
            return
        stack += c
    def one(c:str, id_line:int=None)->None:
        nonlocal stack
        nonlocal stash
        nonlocal automate
        # print(f"1: {c}\t{stack}\t{stash}")
        if stack + c in [op[:len(stack)+1] for op in operators if len(op)>len(stack)]:
            stack += c
            return
        if stack in operators:
            tok_append(id_line)
            automate = zero
            zero(c,id_line)
            return
        tokens.pop()
        stack = stash + stack
        automate = zero
        zero(c,id_line)
        automate = zero
    def two(c: str, id_line:int=None)->None:
        nonlocal stack
        nonlocal stash
        nonlocal automate
        if c == '"': # Si on reconnaît la fin d'une chaîne de caractères, on ajoute tout ça à la suite des tokens
            stack += c
            tok_append(id_line)
            stack = ""
            automate = zero
        else:
            stack += c
    automate = zero
    comment = False
    if not os_isfile(nomFichier):
        print(f"Le fichier '{nomFichier}' n'existe pas", file=stderr)
        exit(1)
    with open(nomFichier, 'r') as f:
        id_line = 1
        for line in f:
            for c in line:
                if comment:
                    comment = False
                    if c == '-':
                        id_line += 1
                        break
                    automate('-',id_line)
                elif c == '-':
                    comment = True
                    continue 
                automate(c,id_line)
            id_line += 1
        tok_append(id_line-1)
        return (tokens,lexique)

if __name__=="__main__":
    from sys import argv
    try:
        tokens: list[Token]
        lexique: list[str]
        if len(argv)>1:
            tokens, lexique = analyseurLexical(argv[1])
        else:
            tokens, lexique = analyseurLexical()
        print()
        for tok in tokens:
            print(tok)
        print()
        for i in range(len(lexique)):
            print(i, lexique[i])
    except Exception as e:
        print(e)
        
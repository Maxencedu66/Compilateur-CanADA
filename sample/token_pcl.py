from sys import stderr
# Définition de la taille max d'un identificateur
MAX_IDENT_SIZE = 40

# Définition de la taille max d'une constante
MAX_CONST_SIZE = 10

# Définition du code des identificateurs et constantes :
STR_CODE = 202
CONST_CODE = 200

# Liste des mots-clés
keywords = [
    'access', 'and', 'begin', 'else', 'elsif', 'end',
    'false', 'for', 'function', 'if', 'in', 'is',
    'loop', 'new', 'not', 'null', 'or', 'out',
    'procedure', 'record', 'rem', 'return', 'reverse', 'then',
    'true', 'type', 'use', 'while', 'with', 'val',
]

# Liste des opérateurs
operators = [
    '=', '/=', '>', '>=', '<', '<=', '+', '-',
    '*', '/', '--', '.', ';',':=','(',')',',',':'
]

def prio_op(op:int)->int:
    if op in (117, 102):
        return 0
    if op<=2:
        return 1
    if op<=6:
        return 2
    if op<=8:
        return 3
    if op<=10 or op==121:
        return 4
    return -1

codes = dict()  # Dictionnaire des codes des mots-clés et opérateurs
for i in range(len(operators)):
    codes[operators[i]] = i+1
for i in range(len(keywords)):
    codes[keywords[i]] = i+101

keys = list(codes.keys())
values = list(codes.values())

def get_keyword(code:[int, tuple]) -> str:
    if isinstance(code, tuple):
        return tuple([get_keyword(c) for c in code])
    if code in (CONST_CODE, STR_CODE):
        return 'const'
    return keys[values.index(code)] if code<300 else 'ident'

class Token:
    """
    Représente un Token par sa valeur et son code (cf. cours p.4-5)
    0: unite lexicale generic
    1-99: operateurs
    100-: keywords

    How to use:
    >>> t = Token('and')
    >>> t
    Token(102, 'and')
    >>> t == 102
    True
    >>> t == 'and'
    True
    >>> t == 'or'
    False
    >>> t == Token('or')
    False
    >>> print(t)
    (102, 'and')
    >>> t != 102
    False
    >>> t != 'and'
    False
    >>> t != 'or'
    True
    >>> t != Token('or')
    True
    """
    has_lexical_error = False
    def __init__(self, value:str, line:int=None, code:int=None) -> None:
        """
        Initialise un Tokenœ

        Args:
            value (str): la valeur du Token
            code (int, optional): le code du Token. Si code==None, utilise le code défini dans fichierReader.py.
        """
        self.value = value
        if line:
            self.line = line+1
        if code is not None:
            self.code = code
        else:
            if value.startswith('"') and value.endswith('"'):
                self.code = STR_CODE
            else:
                self.code = codes.get(value, 0)
                if self.code == 0:
                    if self.value.isdigit() and len(self.value) <= MAX_CONST_SIZE:
                        self.code = CONST_CODE
                    else :
                        print("Erreur lexicale à la ligne", self.line-1, ":", self.value, file=stderr)
                        Token.has_lexical_error = True

    def __str__(self) -> str:
        if self.code == CONST_CODE :
            return f"('const', '{self.value}')"
        elif self.code == STR_CODE :
            return f"('str', '{self.value}')"
        elif self.code >= 300:
            return f"('{self.value}', {self.code-300})"
        else :
            return f"({self.code}, '{self.value}')"
    
    def __repr__(self) -> str:
        return "Token" + self.__str__()
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Token):
            return self.code == other.code and self.value == other.value
        if isinstance(other, int):
            return self.code == other
        if isinstance(other, str):
            return self.value == other
        return False
    def __gt__(self, other) -> bool:
        if isinstance(other, Token):
            return self.code > other.code
        if isinstance(other, int):
            return self.code > other
        return False
    def __lt__(self, other) -> bool:
        if isinstance(other, Token):
            return self.code < other.code
        if isinstance(other, int):
            return self.code < other
        return False
    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
# Fonction test du fichier src.fichierReader
import unittest
from sample.analyseurLexical import analyseurLexical, Token

nomFichier = "data/hw.ada"

attentes = [
    Token("with", 1, 129), Token("ident", 1, 300), Token(".", 1, 12), Token("ident", 1, 301), Token(";", 1, 13),
    Token("procedure", 2, 119), Token("ident", 2, 302), Token("is", 2, 112),
    Token("begin", 4, 103),
    Token("ident", 5, 303), Token(":=", 5, 14), Token("3", 5, 200),
    Token("if", 6, 110), Token("ident", 6, 303), Token("=", 6, 1), Token("3", 6, 200),
    Token("then", 7, 124), Token("ident", 7, 300), Token(".", 7, 12), Token("ident", 7, 301), Token(".", 7, 12), Token("ident", 7, 304), Token("(", 7, 15), Token("\"Hello, world!\"", 7, 202), Token(")", 7, 16), Token(";", 7, 13),
    Token("else", 8, 104), Token("ident", 8, 300), Token(".", 8, 12), Token("ident", 8, 301), Token(".", 8, 12), Token("ident", 8, 304), Token("(", 8, 15), Token("\"Pas Hello, world!\"", 8, 202), Token(")", 8, 16), Token(";", 8, 13),
    Token("end", 9, 106), Token("if", 9, 110), Token(";", 9, 13),
    Token("end", 10, 106), Token("ident", 10, 302), Token(";", 10, 13),
],[
    str("Ada"), str("Text_IO"), str("Hello"), str("x"), str("Put_Line")
]

class TestAnalyseurLexical(unittest.TestCase):
    def test_ma_fonction(self):
        # Écrire vos tests ici
        result = analyseurLexical(nomFichier)
        print(result)
        self.assertEqual(result, attentes)

if __name__ == "__main__":
    unittest.main()


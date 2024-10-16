# Projet compilateur

L'objectif de ce projet est d'écrire un compilateur d'un langage de haut niveau, en développant toutes les étapes qui le compose, depuis l'analyse lexicale jusqu'à la production de code assembleur ARM. Il s'agit d'un petit fragment du langage Ada.

## Arborescence du Projet

L'arborescence de ce projet suit une structure standard pour faciliter la gestion et le développement.
```
❯ tree
aulagnie2u1
├── README.md
├── data
│   ├── Gantt.xlsx
│   ├── first_tree.png
│   ├── first_tree.svg
│   ├── hw.ada
│   ├── test1_correct.ada
│   ├── test2_erreur_lexical.ada
│   ├── test3_op_logique.ada
│   ├── tree_test1_correct.png
│   └── tree_test1_correct.svg
├── docs
│   ├── CoursTraduction.pdf
│   ├── DEBILEANTLR.g4
│   ├── DEBILEGramophone.g4
│   ├── Gramada.g4
│   └── sujet-Projet-2023-24.pdf
├── makefile
├── presentationTest
│   ├── 1
│   ├── 2
│   ├── 3
│   ├── 4
│   ├── 5
│   ├── 6
│   └── 9
├── rapportOld
│   ├── Rapport_final_PPII1.pdf
│   └── Rapport_final_PPII2.pdf
├── reunions
│   ├── PREP_Reunion091123.pdf
│   ├── PREP_Reunion201023.pdf
│   ├── PREP_Reunion221123.pdf
│   ├── PREP_Reunion251023.pdf
│   ├── reunion091123.pdf
│   ├── reunion201023.pdf
│   ├── reunion251023.pdf
│   └── src
│       ├── CR_Reunion091123.md
│       ├── CR_Reunion201023.md
│       ├── CR_Reunion251023.md
│       ├── PREP_Reunion091123.md
│       ├── PREP_Reunion201023.md
│       ├── PREP_Reunion221123.md
│       └── PREP_Reunion251023.md
├── sample
│   ├── AST.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── AST.cpython-310.pyc
│   │   ├── analyseurLexical.cpython-310.pyc
│   │   ├── grammaire.cpython-310.pyc
│   │   ├── token_pcl.cpython-310.pyc
│   │   └── utils.cpython-310.pyc
│   ├── analyseurLexical.py
│   ├── get_codes.py
│   ├── grammaire.py
│   ├── main.py
│   ├── token_pcl.py
│   └── utils.py
├── test
├── tests
│   ├── __init__.py
│   ├── antlr
│   │   ├── Gramada.g4
│   │   ├── Gramada.old
│   │   ├── code.ada
│   │   └── morph.py
│   ├── test_analyseurLexical.py
│   └── test_analyseurLexical_2.py
└── todo.md

11 directories, 61 files
```

## Tests Unitaires

Vous pouvez trouver les tests unitaires dans le répertoire `tests`. Chaque module à tester a un fichier de test correspondant.

### Comment créer un test

1. Créez un fichier de test dans le répertoire `tests` et nommez-le en utilisant la convention de nommage `test_nomdumodule.py`.

2. Importez le module que vous souhaitez tester. Par exemple, pour tester `module1`, vous pouvez utiliser :
   
```python
from mon_module.module1 import fonction_a_tester
```

Écrivez des méthodes de test en utilisant le module unittest. Par exemple :
```Python
import unittest

class TestModule1Functions(unittest.TestCase):
    def test_fonction_a_tester(self):
        # Écrire le test ici
        self.assertEqual(fonction_a_tester(arg1, arg2), attentes)  # Un exemple de test
```

### Comment executer les tests

Pour exécuter les tests, assurez-vous d'être dans le répertoire racine de votre projet, puis utilisez la commande suivante :

```bash
python3 -m unittest tests.test_analyseurLexical
``````
Cela exécutera le test du module analyseurLexical.

```bash
python -m unittest discover -s tests -p 'test_*.py'
``````
Cela exécutera tous les tests dont les noms de fichiers commencent par "test_".

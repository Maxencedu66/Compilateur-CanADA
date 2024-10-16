#!/bin/bash

# Ce script exécute différents scripts Python en fonction de l'argument passé

# Vérifie si un argument a été fourni
if [ -z "$1" ]; then
    echo "Usage: $0 argument"
    exit 1
fi

# Exécute un script Python différent en fonction de l'argument
case "$1" in
    "1")
        echo "Exécution du script 1 avec 4 erreurs lexical : un smiley, un @da au lieu de ada, un $ comme constante et un begin avec un "ï""
        python3 ../sample/main.py 1
    
        ;;
    "2")
        echo "Exécution du script 2 avec 1 erreur lexical : constante trop grande"
        python3 ../sample/main.py 2
        ;;
    "3")
        echo "Exécution du script 3 avec 1 erreur lexical : identifiant trop grande"
        python3 ../sample/main.py 3
        ;;

    "4")
        echo "Exécution du script 4 avec 1 erreur syntaxique : il manque le \";\" à la fin de la ligne 6"
        python3 ../sample/main.py 4
    ;;

    "5")
        echo "Exécution du script 5 avec 1 erreur syntaxique : \"proceure\" au lieu de \"procedure\" ligne 3"
        python3 ../sample/main.py 5
        ;;

    "6")
        echo "Exécution du script 6 avec 1 erreur syntaxique : \".Text_IO\" au lieu de \"Ada.Text_IO\" ligne 1"
        python3 ../sample/main.py 6
        ;;

    "7")
        echo "Exécution du script 7 avec 4 erreur syntaxique : aireRectangle manque un ; pareil pour perimetreRectangle, manque la déclaration pour la variable valeur et manque le if à la ligne 29," 
        python3 ../sample/main.py 7
        ;;

    "8")
        echo "Exécution du script 8 avec 1 erreur syntaxique : rocedur ligne 3, pas de \"\;\" ligne 7, ligne 4 : fonction, ligne 22 manque le \":\", ligne 23 : ifff, ligne 18 : \"---\", ligne 24 manque la \",\""
        python3 ../sample/main.py 8
        ;;

    "9")
        echo "Exécution du script 9 tout va bien !"
        python3 ../sample/main.py 9
        ;;
    *)

        echo "Argument non reconnu. Utilisez 'script1', 'script2' ou 'script3'."
        ;;
esac

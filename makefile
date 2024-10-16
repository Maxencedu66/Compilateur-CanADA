201023:
	pandoc reunions/src/PREP_Reunion201023.md -o reunions/PREP_Reunion201023.pdf --pdf-engine=pdflatex
	pandoc reunions/src/CR_Reunion201023.md -o reunions/reunion201023.pdf --pdf-engine=pdflatex

251023:
	pandoc reunions/src/PREP_Reunion251023.md -o reunions/PREP_Reunion251023.pdf --pdf-engine=pdflatex
	pandoc reunions/src/CR_Reunion251023.md -o reunions/reunion251023.pdf --pdf-engine=pdflatex

091123:
	pandoc reunions/src/PREP_Reunion091123.md -o reunions/PREP_Reunion091123.pdf --pdf-engine=pdflatex
	pandoc reunions/src/CR_Reunion091123.md -o reunions/reunion091123.pdf --pdf-engine=pdflatex

221123:
	pandoc reunions/src/PREP_Reunion221123.md -o reunions/PREP_Reunion221123.pdf --pdf-engine=pdflatex
	pandoc reunions/src/CR_Reunion221123.md -o reunions/reunion221123.pdf --pdf-engine=pdflatex

# Règle par défaut : génère tous les PDFs
all: clean 201023 251023 091123 221123

# Règle pour nettoyer les fichiers générés
clean:
	rm -f reunions/*.pdf

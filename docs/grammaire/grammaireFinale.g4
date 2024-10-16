FICHIER ->	with ada point textio pointvirgule use ada point textio pointvirgule procedure IDENT is DECLETOILE begin INSTRPLUS end IDENTINTER pointvirgule .
DECL ->	type IDENT DINTEROGATION pointvirgule
|   IDENT VIRGULEIDENTETOILE deuxpoint TYPE DPOINTEGALEXPRINTER pointvirgule
|	PROCEDURE
|	FUNC .
DECLETOILE ->	DECL DECLETOILE
|	.
D ->	access IDENT
|	record CHAMPS CHAMPSPLUS end record pointvirgule .
DINTEROGATION ->	is D
|	.

VIRGULEIDENTETOILE -> virgule IDENT
|   .

DPOINTEGALEXPRINTER -> deuxpointsegal EXPR
|   .

PROCEDURE ->	procedure IDENT PARAMSINTER is DECLETOILE begin INSTR INSTRPLUS end IDENTINTER pointvirgule .
FUNC ->	function IDENT PARAMSINTER return TYPE is DECLETOILE begin INSTR INSTRPLUS end IDENTINTER pointvirgule .
EXPR ->	TERM OPTERMETOILE POINTIDENTINTER .
OPTERMETOILE ->	OP TERM OPTERMETOILE
|	.
TERM ->	int
|	caractere VALEXPR
|	true
|	false
|	null
|	not EXPR
|	moins EXPR
|	IDENT PARENTHESEEXPRVIRGULEEXPRETOILEINTER
|	new IDENT .

POINTIDENTINTER -> point IDENT
| .

PARENTHESEEXPRVIRGULEEXPRETOILEINTER -> ( EXPR VIRGULEEXPRETOILE )
| .

VALEXPR ->	val EXPR
|	.
VIRGULEEXPRETOILE ->	virgule EXPR VIRGULEEXPRETOILE
|	.
INSTR ->	IDENT HELP2
|	return EXPRINTER pointvirgule
|	BEGIN 
|	IF
|	FOR
|	WHILE 
|	int FIN
|	caractere VALEXPR FIN
|	true ;
|	false ;
|	null ;
|	not EXPR FIN
|	moins EXPR FIN
|	new IDENT FIN .

FIN -> OPTERMETOILE point IDENT deuxpointsegal EXPR pointvirgule .


HELP2 ->	deuxpointsegal EXPR pointvirgule
|	( EXPR HELP3 .
HELP3 ->	) HELP
|	virgule EXPR VIRGULEEXPRETOILE ) OPTERMETOILE IDENT deuxpointsegal EXPR pointvirgule .
HELP ->	EXPRPARENTHETOILE pointvirgule
|	IDENT deuxpointsegal EXPR pointvirgule
|	OP TERM OPTERMETOILE IDENT deuxpointsegal EXPR pointvirgule .
EXPRINTER ->	EXPR
|	.
EXPRPARENTHETOILE ->	( EXPR ) EXPRPARENTHETOILE
|	.
INSTRPLUS ->	INSTR INSTRPLUS
|	.
BEGIN ->	begin INSTR INSTRPLUS end .
IF ->	if EXPR then INSTR INSTRPLUS IF_TAIL .
IF_TAIL ->	elsif EXPR then INSTR INSTRPLUS IF_TAIL
|	INSTRPLUSELSEINTER end if .
INSTRPLUSELSEINTER ->	else INSTR INSTRPLUS
|	.
FOR ->	for IDENT in REVERSEINTER EXPR troispoints EXPR loop INSTR INSTRPLUS end loop pointvirgule .
REVERSE ->	reverse .
REVERSEINTER ->	REVERSE
|	.
WHILE ->	while EXPR loop INSTR INSTRPLUS end loop .
CHAMPS ->	IDENT IDENTVIRGULEETOILE : TYPE pointvirgule pointvirgule .
IDENTVIRGULEETOILE ->	virgule IDENT IDENTVIRGULEETOILE
|	.
CHAMPSPLUS ->	CHAMPS CHAMPSPLUS
|	.
TYPE ->	IDENT
|	access IDENT .
PARAMS ->	( PARAM PARAMVIRGULEETOILE ) .
PARAMVIRGULEETOILE ->	pointvirgule PARAM PARAMVIRGULEETOILE
|	.
PARAMSINTER ->	PARAMS
|	.
PARAM ->	IDENT IDENTVIRGULEETOILE : MODEINTER TYPE .
MODEINTER ->	MODE
|	.
MODE ->	in OUT .
OUT ->	out
|	.
OP ->	and THEN
|	or ELSE
|	equal
|	different
|	inferior
|	inferioregal
|	superior
|	superioregal
|	mult
|	division
|	rem
|	plus
|	moins .
THEN ->	then
|	.
ELSE ->	else
|	.
IDENT ->	ident .
IDENTINTER ->	IDENT
|	.
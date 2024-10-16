grammar Gramada;

fICHIER   :  'with Ada.Text_IO; use Ada.Text_IO;\nprocedure' IDENT 'is' dECL*'\nbegin' iNSTR+ 'end' IDENT?';';

dECL      :  'type' IDENT ('is' d)? ';'| pROCEDURE | fUNC;
d        :  'access' IDENT | 'record' cHAMPS+ 'end record;';

pROCEDURE :  'procedure' IDENT pARAMS? 'is' dECL*'\nbegin' iNSTR+ 'end' IDENT?';';

fUNC      :  'function' IDENT pARAMS? 'return' tYPE 'is' dECL*'\nbegin' iNSTR+ 'end' IDENT?';';

eXPR      :  tERM (oP tERM)*;
tERM      :  ENTIER | CHAR  | 'true ;' | 'false ;' | 'null ;' | 'not' eXPR | '-' eXPR |   IDENT '('eXPR (','eXPR)*')'  | CHAR 'val' eXPR | 'new' IDENT;

iNSTR     :  aCCES ':=' eXPR';' | 'return' eXPR? ';' |   IDENT ('('eXPR')')*';' | bEGIN | iF | fOR | wHILE;

bEGIN     :  'begin' iNSTR+ 'end';

iF        :  'if' eXPR 'then' iNSTR+ iF_TAIL;
iF_TAIL   :  'elsif' eXPR 'then' iNSTR+ iF_TAIL | ('else' iNSTR+)? 'end if';


fOR       :  'for' IDENT 'in' 'reverse'? eXPR'...'eXPR'\nloop' iNSTR+ 'end loop;';

wHILE     :  'while' eXPR 'loop' iNSTR+ 'end loop';

cHAMPS    :  IDENT (','IDENT)* ':' tYPE';';
tYPE      :  IDENT | 'access' IDENT;
pARAMS    :  '('pARAM (';'pARAM)*')';
pARAM     :  IDENT (','IDENT)* ':' mODE? tYPE;
mODE      :  'in' | 'in out';

oP        :  '=' | '/=' | '<' | '<=' | '>' | '>=' | '+' | '-' | '*' | '/' | 'rem' | 'and' | 'and then' | 'or' | 'or else';

aCCES     :  IDENT | eXPR'.'IDENT;

// IDENT     :  [a-zA-Z] (ENTIER | CHAR | '_')*;

IDENT: CHAR(ENTIER | CHAR | '_')*;

ENTIER : [0-9]+;
CHAR : [a-zA-Z];
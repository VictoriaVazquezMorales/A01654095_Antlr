grammar Abril;

// Parser
program:
    (declaration|statement|function)*
    ;

declaration:
    CONST INT ident ';' #constIntDecl
    | CONST FLOAT ident ';' #constFloatDecl
    | CONST STRING ident ';' #constStrDecl
    | INT ident ';' #varIntDecl
    | FLOAT ident ';' #varFloatDecl
    | STRING ident ';' #varStrDecl
    ;

statement:
    expr '=' expr ';' #assign
    | IF '(' expr ')' '{' statement* '}' (ELSE '{' statement* '}')? ';' #if_else
    | WHILE '(' expr ')' '{' statement* '}' ';' #while
    | ID '('( ID? | ID(',' ID)* )')' ';' #functionCall
;

function:
    FUNC data_type ID '(' ( data_type ident? | data_type ident(','data_type ident)* ) ')'
    '{' (statement|declaration)* RETURN ident';' '}' ';' #func_def
;

ident:
    ID ( '=' expr ) ?
    ;

data_type:
    INT #int
    | FLOAT #float_dt
    | STRING #str_dt
    ;

expr:
    'sqrt' '('expr')' #sqrt
    | expr '**' expr  #power
    | expr '*' expr   #mult
    | expr '/' expr   #div
    | expr '+' expr   #add
    | expr '-' expr   #sub
    | expr '==' expr   #equal
    | expr '>=' expr   #greaterEq
    | expr '<=' expr   #lessEq
    | ID              #id
    | INTEGER         #integer
    | DEC             #float
    | STR     #string
    ;


// Lexer
CONST: 'const';
INT: 'int';
FLOAT: 'float';
STRING: 'str';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FUNC: 'func';
RETURN: 'return';

ID: [a-zA-Z]+;
INTEGER: [0-9]+;
DEC: [0-9]+.{1}[0-9]+;
STR: '"' ~["]* '"';

WS : [ \t\n\r]+ -> skip;
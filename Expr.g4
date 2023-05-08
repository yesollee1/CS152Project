grammar Expr;

prog: expr EOF;

expr: '(' expr ')'                        #parensExpr
    | <assoc=right> left=expr op='^' right=expr         #infixExpr
    | left=expr op=('*'|'/') right=expr   #infixExpr
    | left=expr op=('+'|'-') right=expr   #infixExpr
    | '-' INT                             #negNumberExpr
    | INT                                 #numberExpr
    ;

OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
OP_EXP: '^';

NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;
WS      : [ \t\r\n] -> channel(HIDDEN);

from lark import Lark

grammar = r"""
    start: statements

statements: statement*

statement: loop
         | repeat
         | command
         | conditional
         | function
         | main

loop: "for" identifier "in" "range" "(" range_values ")" block

repeat: "REPETIR" num block

conditional: if_statement
           | while_statement

if_statement: "if" condition block

while_statement: "while" condition block

function: function_definition
        | function_call

function_definition: "def" identifier "(" parameters? ")" block

function_call: identifier "(" arguments? ")"

main: "INICIO" block

command: turtle_command
       | "GROSOR" num

turtle_command: "ADELANTE" num
              | "ATRAS" num
              | "DERECHA" num
              | "IZQUIERDA" num
              | "SOLTAR"
              | "MARCAR"

condition: expr logical_ops

logical_ops: (logical_op expr)*

logical_op: "and" | "or" | "<" | ">" | "==" | "!=" | ">=" | "<="

expr: CNAME
    | num
    | "!" expr
    | expr arithmetic_op expr

arithmetic_op: "+" | "-" | "*" | "/" | "%"

range_values: num ("," num)*

parameters: parameter ("," parameter)*

arguments: argument ("," argument)*

parameter: identifier

argument: expr

identifier: CNAME
num: SIGNED_NUMBER

block: "{" statements "}"


%import common.CNAME
%import common.SIGNED_NUMBER
%import common.WS
%ignore WS
"""

# Configuración del parser
parser = Lark(grammar, start='start', maybe_placeholders=False)

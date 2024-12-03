from lark import Lark, Transformer, v_args
import turtle
import sys
import os

from gramatica.gramatica import parser
from interprete.interprete import LogoInterpreter
from generador.generador_codigo import generate_python_file
from consola.mensaje import print_logo_banner, mensaje_error

# Función para ejecutar el intérprete
def run_logo_interpreter(code):
    interpreter = LogoInterpreter()
    parse_tree = parser.parse(code)
    interpreter.transform(parse_tree)
    turtle.done()

def main():
    print_logo_banner()

    if len(sys.argv) != 2:
        print("Uso: python grama.py <archivo.hlogo>")
        mensaje_error("Error: Debe ingresar un archivo de código High-LOGO")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file + ".py"

    with open(input_file, 'r') as f:
        hlogo_code = f.read()

    generate_python_file(hlogo_code, output_file)
    os.system(f"python {output_file}")

if __name__ == "__main__":
    main()
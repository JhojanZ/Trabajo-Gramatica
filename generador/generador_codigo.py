import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from consola.mensaje import mensaje_error


def generate_python_file(hlogo_code, output_file):
    with open(output_file, 'w') as f:
        f.write("import turtle\n")
        f.write("t = turtle.Turtle()\n")
        f.write("s = turtle.Screen()\n")
        f.write("s.title('Logo Interpreter')\n")
        f.write("\n")
        
        indent_level = 1
        functions = {}
        func_body = []
        current_function = None

        for line in hlogo_code.splitlines():

            line = line.strip()
            if line.startswith("INICIO"):
                if current_function:
                    functions[current_function] = func_body
                func_body = []
                current_function = "main"
                indent_level = 1
            elif any(line.startswith(func) for func in functions.keys()):
                func_body.append(f"{'    ' * indent_level}{line}()\n")
                    
            elif line.startswith("PARA"):
                var, range_args = line.split()[1], line.split('(')[1].split(')')[0].split(',')
                func_body.append(f"for {var} in range({','.join(range_args)}):\n")
                indent_level += 1
            elif line.startswith("REPETIR"):
                repeat_count = line.split()[1]
                func_body.append(f"{'    ' * indent_level}for _ in range({repeat_count}):\n")
                indent_level += 1
            elif line.startswith("{"):
                pass
            elif line.startswith("}"):
                indent_level -= 1
                if indent_level == 0 and current_function is None:
                    func_body.append("\n")
            elif line.startswith("if"):
                condition = line.split(' ', 1)[1].rstrip('{').strip()
                func_body.append(f"{'    ' * indent_level}if {condition}:\n")
                indent_level += 1
            elif line.startswith("func"):
                if current_function:
                    functions[current_function] = func_body
                func_name = line.split()[1].split('(')[0]
                func_body = []
                current_function = func_name
                indent_level = 1
            elif line.startswith("LLAMAR"):
                func_call = line.split(' ', 1)[1]
                if current_function:
                    func_body.append(f"{'    ' * indent_level}{func_call}\n")
                else:
                    func_body.append(f"{'    ' * indent_level}{func_call}\n")
            elif current_function:
                if line.startswith("ADELANTE"):
                    distance = line.split(' ', 1)[1]
                    func_body.append(f"{'    ' * indent_level}t.forward({distance})\n")
                elif line.startswith("ATRAS"):
                    distance = line.split(' ', 1)[1]
                    func_body.append(f"{'    ' * indent_level}t.backward({distance})\n")
                elif line.startswith("DERECHA"):
                    angle = line.split(' ', 1)[1]
                    func_body.append(f"{'    ' * indent_level}t.right({angle})\n")
                elif line.startswith("IZQUIERDA"):
                    angle = line.split(' ', 1)[1]
                    func_body.append(f"{'    ' * indent_level}t.left({angle})\n")
                elif line.startswith("SOLTAR"):
                    func_body.append(f"{'    ' * indent_level}t.penup()\n")
                elif line.startswith("MARCAR"):
                    func_body.append(f"{'    ' * indent_level}t.pendown()\n")
                elif line.startswith("GROSOR"):
                    grosor = line.split(' ', 1)[1]
                    func_body.append(f"{'    ' * indent_level}t.width({grosor})\n")
                elif line.startswith("SET"):
                    var, value = line.split()[1], ' '.join(line.split()[3:])
                    func_body.append(f"{'    ' * indent_level}{var} = {value}\n")
                elif line.startswith("}"):
                    indent_level -= 1
                    if indent_level == 0:
                        func_body.append("\n")
                else:
                    pass
                    # mensaje_error(f"Error: comando no reconocido '{line}'")
             

        if current_function:
            functions[current_function] = func_body

        for func_name, func_body in functions.items():
            f.write(f"def {func_name}():\n")
            for line in func_body:
                f.write(line)
            f.write("\n")

        f.write("\n")
        f.write("main()\n")
        f.write("turtle.done()\n")
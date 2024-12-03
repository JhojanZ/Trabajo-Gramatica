# Función para generar el archivo .py
def generate_python_file(hlogo_code, output_file):
    with open(output_file, 'w') as f:
        f.write("import turtle\n")
        f.write("t = turtle.Turtle()\n")
        f.write("s = turtle.Screen()\n")
        f.write("s.title('Logo Interpreter')\n")
        indent_level = 0

        for line in hlogo_code.splitlines():
            line = line.strip()
            if line.startswith("PARA"):
                var, range_args = line.split()[1], line.split('(')[1].split(')')[0].split(',')
                f.write(f"for {var} in range({','.join(range_args)}):\n")
                indent_level += 1
            elif line.startswith("REPETIR"):
                repeat_count = line.split()[1]
                f.write(f"{'    ' * indent_level}for _ in range({repeat_count}):\n")
                indent_level += 1
            elif line.startswith("{"):
                pass
            elif line.startswith("}"):
                indent_level -= 1
            else:
                if line.startswith("ADELANTE"):
                    distance = line.split()[1]
                    f.write(f"{'    ' * indent_level}t.forward({distance})\n")
                elif line.startswith("ATRAS"):
                    distance = line.split()[1]
                    f.write(f"{'    ' * indent_level}t.backward({distance})\n")
                elif line.startswith("DERECHA"):
                    angle = line.split()[1]
                    f.write(f"{'    ' * indent_level}t.right({angle})\n")
                elif line.startswith("IZQUIERDA"):
                    angle = line.split()[1]
                    f.write(f"{'    ' * indent_level}t.left({angle})\n")
                elif line.startswith("SOLTAR"):
                    f.write(f"{'    ' * indent_level}t.penup()\n")
                elif line.startswith("MARCAR"):
                    f.write(f"{'    ' * indent_level}t.pendown()\n")
                elif line.startswith("GROSOR"):
                    GROSOR = line.split()[1]
                    f.write(f"{'    ' * indent_level}t.GROSOR({GROSOR})\n")
                elif line.startswith("SET"):
                    var, value = line.split()[1], line.split()[3]
                    f.write(f"{'    ' * indent_level}{var} = {value}\n")
        f.write("turtle.done()\n")
from turtle import Turtle, Screen
from lark import Transformer

class LogoInterpreter(Transformer):
    def __init__(self):
        self.variables = {}
        self.turtle = Turtle()
        self.screen = Screen()
        self.screen.title("Logo Interpreter")
        self.pen_is_up = False

    def start(self, items):
        for item in items:
            if item:
                item

    def for_loop(self, items):
        self._handle_for_loop(items)

    def repeat(self, items):
        self._handle_repeat(items)
    
    def debug(self, items):
        self._console(items)

    def turtle_command_fd(self, items):
        self._handle_turtle_command_fd(items)

    def turtle_command_bk(self, items):
        self._handle_turtle_command_bk(items)

    def turtle_command_rt(self, items):
        self._handle_turtle_command_rt(items)

    def turtle_command_lt(self, items):
        self._handle_turtle_command_lt(items)

    def turtle_command_pu(self, items):
        self._handle_turtle_command_pu(items)

    def turtle_command_pd(self, items):
        self._handle_turtle_command_pd(items)

    def command_GROSOR(self, items):
        self._handle_command_GROSOR(items)

    def command_other(self, items):
        self._handle_command_other(items)

    def variable_assignment(self, items):
        self._handle_variable_assignment(items)

    def evaluate_condition(self, items):
        return self._handle_evaluate_condition(items)

    def evaluate_expression(self, items):
        return self._handle_evaluate_expression(items)

    # Métodos privados para manejar cada tipo de comando y estructura

    def _handle_for_loop(self, items):
        var = items[0]
        range_args = items[1:-1]
        body = items[-1]
        if len(range_args) == 1:
            start = 0
            end = int(range_args[0])
            step = 1
        elif len(range_args) == 2:
            start = int(range_args[0])
            end = int(range_args[1])
            step = 1
        elif len(range_args) == 3:
            start = int(range_args[0])
            end = int(range_args[1])
            step = int(range_args[2])
        else:
            return
        for value in range(start, end, step):
            self.variables[var] = value
            for stmt in body:
                stmt

    def _handle_repeat(self, items):
        repeat_count = int(items[0])
        body = items[1:]
        for _ in range(repeat_count):
            for stmt in body:
                stmt

    def _handle_turtle_command_fd(self, items):
        distance = int(items[0])
        if self.pen_is_up:
            self.turtle.pendown()  # Baja la pluma si está levantada
            self.pen_is_up = False
        self.turtle.forward(distance)  # Avanza dibujando

    def _handle_turtle_command_bk(self, items):
        distance = int(items[0])
        if self.pen_is_up:
            self.turtle.pendown()  # Baja la pluma si está levantada
            self.pen_is_up = False
        self.turtle.backward(distance)  # Retrocede dibujando

    def _handle_turtle_command_rt(self, items):
        angle = int(items[0])
        self.turtle.right(angle)

    def _handle_turtle_command_lt(self, items):
        angle = int(items[0])
        self.turtle.left(angle)

    def _handle_turtle_command_pu(self, items):
        self.turtle.penup() 
        self.pen_is_up = True

    def _handle_turtle_command_pd(self, items):
        self.turtle.pendown() 
        self.pen_is_up = False

    def _handle_command_GROSOR(self, items):
        GROSOR = int(items[0])
        self.turtle.GROSOR(GROSOR)

    def _handle_command_other(self, items):
        pass

    def _handle_variable_assignment(self, items):
        var = items[1]
        value = self._handle_evaluate_expression(items[3])
        self.variables[var] = value

    def _handle_evaluate_condition(self, items):
        if len(items) == 1:
            return self._handle_evaluate_expression(items[0])
        else:
            left = self._handle_evaluate_expression(items[0])
            op = items[1]
            right = self._handle_evaluate_expression(items[2])
            if op == 'and':
                return left and right
            elif op == 'or':
                return left or right
            elif op == '<':
                return left < right
            elif op == '>':
                return left > right
            elif op == '==':
                return left == right
            elif op == '!=':
                return left != right
            elif op == '>=':
                return left >= right
            elif op == '<=':
                return left <= right

    def _handle_evaluate_expression(self, items):
        if isinstance(items, list):
            if len(items) == 1:
                return self._handle_evaluate_expression(items[0])
            elif len(items) == 2 and items[0] == '!':
                return not self._handle_evaluate_expression(items[1])
            elif len(items) == 3:
                left = self._handle_evaluate_expression(items[0])
                op = items[1]
                right = self._handle_evaluate_expression(items[2])
                if op == '+':
                    return left + right
                elif op == '-':
                    return left - right
                elif op == '*':
                    return left * right
                elif op == '/':
                    return left / right
                elif op == '%':
                    return left % right
        else:
            if isinstance(items, int):
                return items
            elif isinstance(items, str):
                if items in self.variables:
                    return self.variables[items]
                else:
                    return items
            else:
                return items
        
    def _console(items):
        print(items)
    
    

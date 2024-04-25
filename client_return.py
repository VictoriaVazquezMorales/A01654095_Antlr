from antlr4 import *
from antlr.AbrilLexer import AbrilLexer
from antlr.AbrilParser import AbrilParser
from antlr.AbrilListener import AbrilListener
from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}:{column}: {msg}")

class VariableDeclarationListener(AbrilListener):
    def _init_(self):
        self.variables = set()

    def enterVarDeclaration(self, ctx):
        var_name = ctx.ID().getText()
        self.variables.add(var_name)

    def enterVariable(self, ctx):
        var_name = ctx.ID().getText()
        if var_name not in self.variables:
            print(f"Error: Variable '{var_name}' used without being declared.")


class ArithmeticExpressionListener(AbrilListener):
    def _init_(self):
        pass

    def enterArithmeticExpr(self, ctx):
        # Suponiendo que los nodos hijos son los operadores y operandos de la expresión aritmética
        num_operands = len(ctx.children)
        if num_operands < 3:
            raise Exception("Error: Arithmetic expression is incomplete.")

        # Validar tipos y operaciones aritméticas
        operator = ctx.getChild(1).getText()
        operand_types = [child.dataType().getText() for child in ctx.children[::2]]

        # Realizar validación bottom-up
        if operator in ['+', '-', '*', '/']:
            # Suponiendo que solo se permiten operaciones entre números enteros o de punto flotante
            valid_types = {'int', 'float'}
            for op_type in operand_types:
                if op_type not in valid_types:
                    raise Exception(f"Error: Arithmetic expression contains unsupported type '{op_type}'.")
            result_type = 'int' if 'int' in operand_types else 'float'

class FunctionReturnListener(AbrilListener):
    def _init_(self):
        self.functions = {}

    def enterFunctionDeclaration(self, ctx):
        func_name = ctx.ID().getText()
        return_type = ctx.dataType().getText()
        self.functions[func_name] = return_type

    def enterReturnStatement(self, ctx):
        func_name = ctx.ID().getText()
        return_expr_type = ctx.expr().dataType().getText()
        if func_name in self.functions:
            declared_return_type = self.functions[func_name]
            if return_expr_type != declared_return_type:
                print(f"Error: Return type mismatch in function '{func_name}'. Expected '{declared_return_type}', got '{return_expr_type}'.")

def main(file_path):
    input_stream = FileStream(file_path)
    lexer = AbrilLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AbrilParser(stream)
    tree = parser.program()

    # Crear e instanciar los listeners de validación
    var_listener = VariableDeclarationListener()
    arith_expr_listener = ArithmeticExpressionListener()
    return_listener = FunctionReturnListener()

    # Recorrer el árbol con los listeners
    walker = ParseTreeWalker()
    walker.walk(var_listener, tree)
    walker.walk(arith_expr_listener, tree)
    walker.walk(return_listener, tree)

if __name__ == '__main__':
    main('test_return.txt')

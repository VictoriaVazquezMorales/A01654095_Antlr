from antlr4 import *
from antlr.AbrilLexer import AbrilLexer
from antlr.AbrilParser import AbrilParser
from antlr.AbrilListener import AbrilListener

class VariableCheckListener(AbrilListener):
    def __init__(self):
        self.declared_variables = set()
        self.errors = []

    def enterVarIntDecl(self, ctx):
        var_name = ctx.ident().ID().getText()
        if var_name in self.declared_variables:
            self.errors.append(f"Variable '{var_name}' ya ha sido declarada.")
        else:
            self.declared_variables.add(var_name)

    def enterAssign(self, ctx):
        var_name = ctx.expr(0).getText()
        if var_name not in self.declared_variables:
            self.errors.append(f"Variable '{var_name}' no ha sido declarada antes de su uso.")

# Crea un objeto de entrada (input) y el lexer
input_stream = FileStream("test_decl.txt")
lexer = AbrilLexer(input_stream)

# Crea el parser
tokens = CommonTokenStream(lexer)
parser = AbrilParser(tokens)

# Analiza el programa
tree = parser.program()

# Crea el Listener y recorre el árbol
listener = VariableCheckListener()
walker = ParseTreeWalker()
walker.walk(listener, tree)

# Imprime errores encontrados
if listener.errors:
    for error in listener.errors:
        print(error)
else:
    print("No se encontraron errores de declaración.")

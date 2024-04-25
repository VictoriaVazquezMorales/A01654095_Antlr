import sys
from antlr4 import *
from antlr.AbrilLexer import AbrilLexer
from antlr.AbrilParser import AbrilParser
from antlr.AbrilVisitor import AbrilVisitor


class VariableCheckVisitor(AbrilVisitor):
    def __init__(self):
        self.declared_vars = set()
        self.undefined_vars = set()

    def visitVarIntDecl(self, ctx):
        var_name = ctx.ident().ID().getText()
        self.declared_vars.add(var_name)

    def visitVarFloatDecl(self, ctx):
        var_name = ctx.ident().ID().getText()
        self.declared_vars.add(var_name)

    def visitVarStrDecl(self, ctx):
        var_name = ctx.ident().ID().getText()
        self.declared_vars.add(var_name)

    def visitConstIntDecl(self, ctx):
        var_name = ctx.ident().ID().getText()
        self.declared_vars.add(var_name)

    def visitConstFloatDecl(self, ctx):
        var_name = ctx.ident().ID().getText()
        self.declared_vars.add(var_name)

    def visitConstStrDecl(self, ctx):
        var_name = ctx.ident().ID().getText()
        self.declared_vars.add(var_name)

    def visitAssign(self, ctx):
        # Verificar el lado izquierdo de la asignación
        var_name = ctx.expr(0).getText()
        if var_name not in self.declared_vars:
            self.undefined_vars.add(var_name)

    def visitFunctionCall(self, ctx):
        # Verificar si las variables en la llamada a función están declaradas
        for i in range(ctx.ID().getChildCount()):
            var_name = ctx.ID(i).getText()
            if var_name not in self.declared_vars:
                self.undefined_vars.add(var_name)

    def report(self):
        if not self.undefined_vars:
            print("Todas las variables están declaradas correctamente.")
        else:
            print("Variables no declaradas previamente:", self.undefined_vars)


def main(input_file):
    input_stream = FileStream(input_file)
    lexer = AbrilLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AbrilParser(stream)
    tree = parser.program()

    visitor = VariableCheckVisitor()
    visitor.visit(tree)

    visitor.report()


if __name__ == "__main__":
    main("test_decl.txt")


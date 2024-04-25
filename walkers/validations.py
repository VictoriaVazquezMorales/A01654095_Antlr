from antlr.AbrilListener import AbrilListener


class Declaration(AbrilListener):

    def __init__(self):
        self.variables = {}

    def enterConstFloatDecl(self, ctx):
        pass

    def enterConstIntDeclDecl(self, ctx):
        pass

    def enterConstStrDeclDecl(self, ctx):
        pass

    def enterVarFloatDeclFloatDecl(self, ctx):
        pass

    def enterVarIntDeclIntDeclDecl(self, ctx):
        pass

    def enterVarStrDeclStrDeclDecl(self, ctx):
        pass

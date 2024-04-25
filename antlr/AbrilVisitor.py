# Generated from /Users/victoriavazquez/Codes/PycharmProjects/A01654095_Antlr/antlr/Abril.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AbrilParser import AbrilParser
else:
    from AbrilParser import AbrilParser

# This class defines a complete generic visitor for a parse tree produced by AbrilParser.

class AbrilVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AbrilParser#program.
    def visitProgram(self, ctx:AbrilParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#constIntDecl.
    def visitConstIntDecl(self, ctx:AbrilParser.ConstIntDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#constFloatDecl.
    def visitConstFloatDecl(self, ctx:AbrilParser.ConstFloatDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#constStrDecl.
    def visitConstStrDecl(self, ctx:AbrilParser.ConstStrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#varIntDecl.
    def visitVarIntDecl(self, ctx:AbrilParser.VarIntDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#varFloatDecl.
    def visitVarFloatDecl(self, ctx:AbrilParser.VarFloatDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#varStrDecl.
    def visitVarStrDecl(self, ctx:AbrilParser.VarStrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#assign.
    def visitAssign(self, ctx:AbrilParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#if_else.
    def visitIf_else(self, ctx:AbrilParser.If_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#while.
    def visitWhile(self, ctx:AbrilParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#functionCall.
    def visitFunctionCall(self, ctx:AbrilParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#func_def.
    def visitFunc_def(self, ctx:AbrilParser.Func_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#ident.
    def visitIdent(self, ctx:AbrilParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#int.
    def visitInt(self, ctx:AbrilParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#float_dt.
    def visitFloat_dt(self, ctx:AbrilParser.Float_dtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#str_dt.
    def visitStr_dt(self, ctx:AbrilParser.Str_dtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#add.
    def visitAdd(self, ctx:AbrilParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#sub.
    def visitSub(self, ctx:AbrilParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#mult.
    def visitMult(self, ctx:AbrilParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#string.
    def visitString(self, ctx:AbrilParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#integer.
    def visitInteger(self, ctx:AbrilParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#float.
    def visitFloat(self, ctx:AbrilParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#div.
    def visitDiv(self, ctx:AbrilParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#equal.
    def visitEqual(self, ctx:AbrilParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#sqrt.
    def visitSqrt(self, ctx:AbrilParser.SqrtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#lessEq.
    def visitLessEq(self, ctx:AbrilParser.LessEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#greaterEq.
    def visitGreaterEq(self, ctx:AbrilParser.GreaterEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#id.
    def visitId(self, ctx:AbrilParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AbrilParser#power.
    def visitPower(self, ctx:AbrilParser.PowerContext):
        return self.visitChildren(ctx)



del AbrilParser
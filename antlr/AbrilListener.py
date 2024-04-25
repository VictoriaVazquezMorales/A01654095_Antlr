# Generated from /Users/victoriavazquez/Codes/PycharmProjects/A01654095_Antlr/antlr/Abril.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AbrilParser import AbrilParser
else:
    from AbrilParser import AbrilParser

# This class defines a complete listener for a parse tree produced by AbrilParser.
class AbrilListener(ParseTreeListener):

    # Enter a parse tree produced by AbrilParser#program.
    def enterProgram(self, ctx:AbrilParser.ProgramContext):
        pass

    # Exit a parse tree produced by AbrilParser#program.
    def exitProgram(self, ctx:AbrilParser.ProgramContext):
        pass


    # Enter a parse tree produced by AbrilParser#constIntDecl.
    def enterConstIntDecl(self, ctx:AbrilParser.ConstIntDeclContext):
        pass

    # Exit a parse tree produced by AbrilParser#constIntDecl.
    def exitConstIntDecl(self, ctx:AbrilParser.ConstIntDeclContext):
        pass


    # Enter a parse tree produced by AbrilParser#constFloatDecl.
    def enterConstFloatDecl(self, ctx:AbrilParser.ConstFloatDeclContext):
        pass

    # Exit a parse tree produced by AbrilParser#constFloatDecl.
    def exitConstFloatDecl(self, ctx:AbrilParser.ConstFloatDeclContext):
        pass


    # Enter a parse tree produced by AbrilParser#constStrDecl.
    def enterConstStrDecl(self, ctx:AbrilParser.ConstStrDeclContext):
        pass

    # Exit a parse tree produced by AbrilParser#constStrDecl.
    def exitConstStrDecl(self, ctx:AbrilParser.ConstStrDeclContext):
        pass


    # Enter a parse tree produced by AbrilParser#varIntDecl.
    def enterVarIntDecl(self, ctx:AbrilParser.VarIntDeclContext):
        pass

    # Exit a parse tree produced by AbrilParser#varIntDecl.
    def exitVarIntDecl(self, ctx:AbrilParser.VarIntDeclContext):
        pass


    # Enter a parse tree produced by AbrilParser#varFloatDecl.
    def enterVarFloatDecl(self, ctx:AbrilParser.VarFloatDeclContext):
        pass

    # Exit a parse tree produced by AbrilParser#varFloatDecl.
    def exitVarFloatDecl(self, ctx:AbrilParser.VarFloatDeclContext):
        pass


    # Enter a parse tree produced by AbrilParser#varStrDecl.
    def enterVarStrDecl(self, ctx:AbrilParser.VarStrDeclContext):
        pass

    # Exit a parse tree produced by AbrilParser#varStrDecl.
    def exitVarStrDecl(self, ctx:AbrilParser.VarStrDeclContext):
        pass


    # Enter a parse tree produced by AbrilParser#assign.
    def enterAssign(self, ctx:AbrilParser.AssignContext):
        pass

    # Exit a parse tree produced by AbrilParser#assign.
    def exitAssign(self, ctx:AbrilParser.AssignContext):
        pass


    # Enter a parse tree produced by AbrilParser#if_else.
    def enterIf_else(self, ctx:AbrilParser.If_elseContext):
        pass

    # Exit a parse tree produced by AbrilParser#if_else.
    def exitIf_else(self, ctx:AbrilParser.If_elseContext):
        pass


    # Enter a parse tree produced by AbrilParser#while.
    def enterWhile(self, ctx:AbrilParser.WhileContext):
        pass

    # Exit a parse tree produced by AbrilParser#while.
    def exitWhile(self, ctx:AbrilParser.WhileContext):
        pass


    # Enter a parse tree produced by AbrilParser#functionCall.
    def enterFunctionCall(self, ctx:AbrilParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by AbrilParser#functionCall.
    def exitFunctionCall(self, ctx:AbrilParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by AbrilParser#func_def.
    def enterFunc_def(self, ctx:AbrilParser.Func_defContext):
        pass

    # Exit a parse tree produced by AbrilParser#func_def.
    def exitFunc_def(self, ctx:AbrilParser.Func_defContext):
        pass


    # Enter a parse tree produced by AbrilParser#ident.
    def enterIdent(self, ctx:AbrilParser.IdentContext):
        pass

    # Exit a parse tree produced by AbrilParser#ident.
    def exitIdent(self, ctx:AbrilParser.IdentContext):
        pass


    # Enter a parse tree produced by AbrilParser#int.
    def enterInt(self, ctx:AbrilParser.IntContext):
        pass

    # Exit a parse tree produced by AbrilParser#int.
    def exitInt(self, ctx:AbrilParser.IntContext):
        pass


    # Enter a parse tree produced by AbrilParser#float_dt.
    def enterFloat_dt(self, ctx:AbrilParser.Float_dtContext):
        pass

    # Exit a parse tree produced by AbrilParser#float_dt.
    def exitFloat_dt(self, ctx:AbrilParser.Float_dtContext):
        pass


    # Enter a parse tree produced by AbrilParser#str_dt.
    def enterStr_dt(self, ctx:AbrilParser.Str_dtContext):
        pass

    # Exit a parse tree produced by AbrilParser#str_dt.
    def exitStr_dt(self, ctx:AbrilParser.Str_dtContext):
        pass


    # Enter a parse tree produced by AbrilParser#add.
    def enterAdd(self, ctx:AbrilParser.AddContext):
        pass

    # Exit a parse tree produced by AbrilParser#add.
    def exitAdd(self, ctx:AbrilParser.AddContext):
        pass


    # Enter a parse tree produced by AbrilParser#sub.
    def enterSub(self, ctx:AbrilParser.SubContext):
        pass

    # Exit a parse tree produced by AbrilParser#sub.
    def exitSub(self, ctx:AbrilParser.SubContext):
        pass


    # Enter a parse tree produced by AbrilParser#mult.
    def enterMult(self, ctx:AbrilParser.MultContext):
        pass

    # Exit a parse tree produced by AbrilParser#mult.
    def exitMult(self, ctx:AbrilParser.MultContext):
        pass


    # Enter a parse tree produced by AbrilParser#string.
    def enterString(self, ctx:AbrilParser.StringContext):
        pass

    # Exit a parse tree produced by AbrilParser#string.
    def exitString(self, ctx:AbrilParser.StringContext):
        pass


    # Enter a parse tree produced by AbrilParser#integer.
    def enterInteger(self, ctx:AbrilParser.IntegerContext):
        pass

    # Exit a parse tree produced by AbrilParser#integer.
    def exitInteger(self, ctx:AbrilParser.IntegerContext):
        pass


    # Enter a parse tree produced by AbrilParser#float.
    def enterFloat(self, ctx:AbrilParser.FloatContext):
        pass

    # Exit a parse tree produced by AbrilParser#float.
    def exitFloat(self, ctx:AbrilParser.FloatContext):
        pass


    # Enter a parse tree produced by AbrilParser#div.
    def enterDiv(self, ctx:AbrilParser.DivContext):
        pass

    # Exit a parse tree produced by AbrilParser#div.
    def exitDiv(self, ctx:AbrilParser.DivContext):
        pass


    # Enter a parse tree produced by AbrilParser#equal.
    def enterEqual(self, ctx:AbrilParser.EqualContext):
        pass

    # Exit a parse tree produced by AbrilParser#equal.
    def exitEqual(self, ctx:AbrilParser.EqualContext):
        pass


    # Enter a parse tree produced by AbrilParser#sqrt.
    def enterSqrt(self, ctx:AbrilParser.SqrtContext):
        pass

    # Exit a parse tree produced by AbrilParser#sqrt.
    def exitSqrt(self, ctx:AbrilParser.SqrtContext):
        pass


    # Enter a parse tree produced by AbrilParser#lessEq.
    def enterLessEq(self, ctx:AbrilParser.LessEqContext):
        pass

    # Exit a parse tree produced by AbrilParser#lessEq.
    def exitLessEq(self, ctx:AbrilParser.LessEqContext):
        pass


    # Enter a parse tree produced by AbrilParser#greaterEq.
    def enterGreaterEq(self, ctx:AbrilParser.GreaterEqContext):
        pass

    # Exit a parse tree produced by AbrilParser#greaterEq.
    def exitGreaterEq(self, ctx:AbrilParser.GreaterEqContext):
        pass


    # Enter a parse tree produced by AbrilParser#id.
    def enterId(self, ctx:AbrilParser.IdContext):
        pass

    # Exit a parse tree produced by AbrilParser#id.
    def exitId(self, ctx:AbrilParser.IdContext):
        pass


    # Enter a parse tree produced by AbrilParser#power.
    def enterPower(self, ctx:AbrilParser.PowerContext):
        pass

    # Exit a parse tree produced by AbrilParser#power.
    def exitPower(self, ctx:AbrilParser.PowerContext):
        pass



del AbrilParser
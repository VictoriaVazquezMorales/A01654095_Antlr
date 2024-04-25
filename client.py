from antlr4 import *
from antlr.AbrilLexer import AbrilLexer
from antlr.AbrilParser import AbrilParser
from antlr.AbrilListener import AbrilListener
from walkers.validations import Declaration


class TreePrinter(AbrilListener):
    pass


def main(argv, walkers=None):
    parser = AbrilParser(CommonTokenStream(AbrilLexer(FileStream(argv))))
    tree = parser.program()
    declarations = Declaration()

    walker = ParseTreeWalker()
    walker.walk(declarations, tree)
    declarations.enterVarDecl(walker)

if __name__ == '__main__':
    main('test1.txt')

class Lexer:
    def __init__(self, syn):
        self.syn = syn
        self.lines = self.syn.split("\n")
        self.tokens = []
        for line in self.lines:
            self.tokens.append(line.split(" "))
        
class Token:
    def __init__(self, token, type):
        self.token = token
        self.type = type


from enum import Enum
class TOKENS(Enum):

    STRING = 1
    NUMBER = 2
    EOF = -1
    NEWLINE = 0
    IDENTIFIER = 3

    ADD = 100
    SUB = 101
    DIV = 110
    MUL = 111
    EQ = 105
    GTEQ = 106
    LTEQ = 104
    GT = 107
    LT = 103
    NOEQ = 102
    EQEQ = 108

    PRINT = 200
    INPUT = 201

def main():
    with open("tests/test1.frg", "r") as f:
        code = f.read()
        lexer = Lexer(code)
        print(lexer.tokens)

main()
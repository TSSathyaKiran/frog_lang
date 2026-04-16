class Lexer:
    def __init__(self, syn):
        self.syn = syn
        self.lines = self.syn.split("\n")
        self.tokens = []
        for line in self.lines:
            self.tokens.append(line.split(" "))

    def getToken(self, preToken):
        token = None
        if preToken == "+":
            token = Token(preToken, TOKENS.ADD)
        elif preToken == "-":
            token = Token(preToken, TOKENS.SUB)
        elif preToken == "*":
            token = Token(preToken, TOKENS.MUL)
        elif preToken == "/":
            token = Token(preToken, TOKENS.DIV)
        elif preToken == "=":
            token = Token(preToken, TOKENS.EQ)
        elif preToken == ">=":
            token = Token(preToken, TOKENS.GTEQ)
        elif preToken == "<=":
            token = Token(preToken, TOKENS.LTEQ)
        elif preToken == ">":
            token = Token(preToken, TOKENS.GT)
        elif preToken == "<":
            token = Token(preToken, TOKENS.LT)
        elif preToken == "!=":
            token = Token(preToken, TOKENS.NOEQ)
        elif preToken == "==":
            token = Token(preToken, TOKENS.EQEQ)
        elif preToken == "print":
            token = Token(preToken, TOKENS.PRINT)
        elif preToken == "input":
            token = Token(preToken, TOKENS.INPUT)
        elif preToken.isdigit():
            token = Token(preToken, TOKENS.NUMBER)
        elif preToken.isidentifier():
            token = Token(preToken, TOKENS.IDENTIFIER)

        elif preToken.startswith('"') and preToken.endswith('"'):
            token = token[1:-1]
            token = Token(preToken, TOKENS.STRING)
            #should add illegal character check here
            #later
        
        elif isinstance(preToken, int) or isinstance(preToken, float):
            token = Token(preToken, TOKENS.NUMBER)
            #idk float in assembly, have to check
        
        

        
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
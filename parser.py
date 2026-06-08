from lexer import *

class parser:
    def __init__(self, lexer, emitter):
        self.lexer = lexer
        self.emitter = emitter

        self.strings = [] # stores the string literals
        self.strCount = 0

        self.symbols    = {} #symbols store names of variables and offsets
        self.nextOffset = 0

        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()

    def checkToken(self, kind):
        return self.curToken.kind == kind
 
    def nextToken(self):
        self.curToken  = self.peekToken
        self.peekToken = self.lexer.getToken()
 
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort(f"expected {kind.name}, got {self.curToken.kind.name}")
        self.nextToken()
 
    def nl(self):
        self.match(TokenType.NEWLINE)
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()
 
    def abort(self, message):
        sys.exit("Parser error: " + message)


    def getOffset(self, name):
        if name not in self.symbols:
            self.abort(f"undefined variable: {name}")
        return self.symbols[name]
    
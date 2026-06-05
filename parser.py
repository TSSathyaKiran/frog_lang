from lexer import *

class parser:
    def __init__(self, lexer, emitter):
        self.lexer = lexer
        self.emitter = emitter

        self.strings = []
        self.strCount = 0

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
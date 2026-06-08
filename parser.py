import sys
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
    

    def printString(self):
        text  = self.curToken.text
        label = f"str_{self.strCount}"
        self.strCount += 1
        self.strings.append((label, text))
        self.nextToken()

        self.emitter.emitLine(f"    adrp x1, {label}")
        self.emitter.emitLine(f"    add  x1, x1, :lo12:{label}")
        self.emitter.emitLine(f"    mov  x2, #{len(text) + 1}")

        self.emitter.emitLine( "    mov  x0, #1")
        self.emitter.emitLine( "    mov  x8, #64")   
        self.emitter.emitLine( "    svc  #0")

        #print in arm64:

        # adrp x1, str_0
        # add  x1, x1, :lo12:str_0
        # mov  x2, #12
        # mov  x0, #1
        # mov  x8, #64
        # svc  #0


    def printStatement(self):
        self.nextToken()
        if self.checkToken(TokenType.STRING):
            self.printString()
 
    def statement(self):
        if self.checkToken(TokenType.PRINT):
            self.printStatement()
        
        self.nl()


    def program(self):

        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()
 
        while not self.checkToken(TokenType.EOF):
            self.statement()

        if self.strings:
            self.emitter.headerLine(".section .data")
            for label, text in self.strings:
                # .asciz automatically null terminates
                self.emitter.headerLine(f'{label}: .asciz "{text}\\n"')
            self.emitter.headerLine("")

        self.emitter.headerLine(".section .text")
        self.emitter.headerLine(".global _start")
        self.emitter.headerLine("")


        self.emitter.headerLine("_start:")

        self.emitter.headerLine("    stp  x29, x30, [sp, #-16]!")
        self.emitter.headerLine("    mov  x29, sp")

        self.emitter.emitLine( "    mov  x0,  #0")  
        self.emitter.emitLine( "    mov  x8,  #93")  
        self.emitter.emitLine( "    svc  #0")

        self.emitter.writeFile()
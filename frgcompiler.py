import sys
from lexer import *
from emitter import *
from parser import *

def main():
    print("Frog Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")

    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()

    lexer   = Lexer(source)
    emitter = Emitter("out.s")
    parser  = Parser(lexer, emitter)

    parser.program()

    print("Done.")

main()
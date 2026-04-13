class Lexer:
    def __init__(self, syn):
        self.syn = syn
        self.lines = self.syn.split("\n")
        self.tokens = []
        for line in self.lines:
            self.tokens.append(line.split(" "))
        

def main():
    with open("tests/test1.frg", "r") as f:
        code = f.read()
        lexer = Lexer(code)
        print(lexer.tokens)

main()
class lexer:
    def __init__(self, code):
        self.line = 1
        self.column = 1
        self.char_pos = 0
        self.code = code
        self.current = ""

    def advance(self):
        self.column += 1
        self.char_pos += 1

        if self.char_pos >= len(self.code):
            self.current = None
        else:
            self.current = self.code[self.char_pos]
        
        if self.current == "\n":
            self.line += 1
            self.column = 0

    def peek(self):
        pass
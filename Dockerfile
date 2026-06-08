FROM ubuntu:latest

RUN apt update && apt install -y --fix-missing python3 binutils

WORKDIR /frog

COPY lexer.py .
COPY emitter.py .
COPY parser.py .
COPY frgcompiler.py .

COPY tests/test1.frg .

RUN python3 frgcompiler.py test1.frg
RUN as -o out.o out.s
RUN ld -o out out.o

CMD ["./out"]
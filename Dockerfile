FROM ubuntu:latest
RUN apt update 
RUN apt install -y binutils gcc
WORKDIR /examples
COPY /examples/example1.s /examples/example1.s
RUN gcc -nostdlib example1.s -o example1
CMD ["./example1"]
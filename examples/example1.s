.section .data
str_0: .asciz "hello world\n"

.section .text
.global _start

_start:
    stp  x29, x30, [sp, #-16]!
    mov  x29, sp
    sub  sp,  sp,  #16

    adrp x1, str_0
    add  x1, x1, :lo12:str_0
    mov  x2, #12
    mov  x0, #1
    mov  x8, #64
    svc  #0

    add  sp,  sp,  #16
    ldp  x29, x30, [sp], #16
    mov  x0,  #0
    mov  x8,  #93
    svc  #0
.global _start
.section .text
_start:
    mov x0, #1
    mov x1, #2
    add x2, x1, x0
    mov x3, #1
    mov x8, #64
    svc #0

    mov x0, #0
    mov x8, #93
    svc #0
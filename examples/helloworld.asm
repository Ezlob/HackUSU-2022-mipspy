.data
hello_msg: .asciiz "\nHello Friend.\n\n"


.text
main:
    la      $a0, hello_msg
    jal     print_string
    j       terminate


print_string:
    li      $v0, 4
    syscall
    jr      $ra

terminate:
    li      $v0, 10
    syscall
// This file is part of
// File name: vm_code/code/Factorial.asm

// Computes the factorial of a number stored in R0 and stores the result in R2.
// (R0, R1 and R2 refer to RAM[0], RAM[1] and RAM[2], respectively.)

(INIT)      // set up all needed registers
    @R0
    D=M
    @END
    D;JLE   // do nothing if R0 stores zero or a negative number

    @R2
    M=0     // set R2 for storing the partial and final results

    @R0
    MD=M-1
    @R1     // set R0 and R1 to start the multiplication loop
    M=D+1
    @acc    // decreasing accumulator
    M=D //-1   // starts at R1 - 2

(MULTLOOP)      // multiplication loop
    @R0
    D=M
    @FACLOOP
    D;JEQ   // jump to END if R0 = 0

//  @R2
//  D=M
//  @R1
//  D=D+M
//  @R2
//  M=D
    @R1
    D=M
    @R2
    M=D+M

    @R0
    M=M-1
    @MULTLOOP
    0;JMP   // goto the top of the loop

(FACLOOP)   // FIXME: does R2 need to be set to zero after every MULTLOOP iteration?
    @acc
    MD=M-1
    @R0
    M=D     // acc is decreased and stored at R0

    @END
    D;JLE // goto to END if acc =< 0

    @R2
    D=M
    M=0     // R2 is set to zero again
    @R1
    M=D     // R2 is stored in R1

    @MULTLOOP
    0;JMP

(END)
    @END
    0;JMP

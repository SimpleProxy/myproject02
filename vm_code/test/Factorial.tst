// This file is part of
// File name: vm_code/test/Factorial.tst

load "../code/Factorial.asm",
output-file Factorial.out,
//compare-to Factorial.cmp,
output-list RAM[0]%D2.6.2 RAM[2]%D2.6.2;

set PC 0,
set RAM[0] 500,   // Set test arguments
set RAM[1] 500,
set RAM[2] -1;  // Ensure that program initialized product to 0
repeat 500000 {
  ticktock;
}
set RAM[0] 0,   // Restore arguments in case program used them as loop counter
set RAM[1] 500,
output;


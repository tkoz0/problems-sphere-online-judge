memory diagram

C__MA_A_A_A_A_A_A_A_A_A__MB_B_B_B_B__

C = line counter
A = string A
B = string B
M = marker cells, value 1 to mark beginning of strings

++++ ++++ ++++ ++++ ++++ ++++ 24 input lines (counter)
[- decrement C
    input string A
    >>>>,>>,>>,>>,>>,>>,>>,>>,>>,>>, pointer at last A
    input string B
    >>>>,>>,>>,>>,>>, pointer at last B
    >,[-] discard newline character
]

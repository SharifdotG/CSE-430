# CSE 430: Compiler Design - Lab Work 3

## Introduction

Write a program for lexical analysis i.e. takes a line from file or keyboard and specify each word or character into the following tokens. The lexical analyzer should ignore redundant spaces, tabs and newlines.

- Any word either combination of characters and digits or combination of characters: Identifier.
- Any number : Constant
- Parenthesis : ( ), , [ ]
- Punctuation sign : ;(semicolon) , : (colon) , , (coma)
- Arithmetic Operator : + , -, *, /
- Logical Operator : >, >=, <, <=, ==, ! =
- Keyword: There are total 32 keywords in C
- Comments: Single Line Comment in C

## Input

```c
void main()
{
    int a, b, c;
    //comment
    int a = b*c + 10;
    if(a!=2)
        a = 0;
}

```

## Output

```plaintext
1 void keyword
1 main identifier
1 ( parenthesis
1 ) parenthesis
2 { parenthesis
3 int keyword
3 a identifier
3 , punctuation
3 b identifier
3 , punctuation
3 c identifier
3 ; punctuation
4 //comment comment
5 int keyword
5 a identifier
5 = assign_op
5 b identifier
5 * arithmetic_op
5 c identifier
5 + arithmetic_op
5 10 constant
5 ; punctuation
6 if keyword
6 ( parenthesis
6 a identifier
6 != logical_op
6 2 constant
6 ) parenthesis
7 a identifier
7 = assign_op
7 0 constant
7 ; punctuation
8 } parenthesis
```

## Implementation Details

Use flex to implement the lexical analyzer. The flex file should contain rules to identify the tokens as specified above. The program should read input from a file or standard input and output the tokens along with their line numbers and types.

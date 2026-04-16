# CSE 430 Lab Works

This repository contains simple Python and Flex implementations for CSE 430 Compiler Design lab tasks.

## Folder Structure

- `Lab Work 1/`
  - `Lab_Work_1.md`
  - `lab1_lexical_analyzer.py`
- `Lab Work 2/`
  - `Lab_Work_2.md`
  - `lab2_symbol_table.py`
- `Lab Work 3/`
  - `Lab_Work_3.md`
  - `lab3_lexical_analyzer.l`
  - `sample_input_3.c`

## Lab Work 1

Topic: Lexical analysis

Run from `Lab Work 1`:

```bash
py lab1_lexical_analyzer.py sample_input_1.c
```

or

```bash
py lab1_lexical_analyzer.py sample_input_2.c
```

## Lab Work 2

Topic: Symbol table using hashing with chaining

Important notes:

- Uses only manual console input
- Does not use Python built-in `dict`
- Does not use any linked-list library
- Uses a custom node class and chaining through `next`

Run from `Lab Work 2`:

```bash
py lab2_symbol_table.py
```

Then enter 6 tuples in this format:

```text
NAME, TYPE, SIZE, DIMENSION, LINE, ADDRESS
```

Example:

```text
x, ID, 2, 1, 5, 0x0FF
```

After the 6 initial tuples are inserted, use the menu to show, search, insert, update, or delete symbols.

## Lab Work 3

Topic: Lexical analysis using Flex (Linux/MacOS Only!)

Run from `Lab Work 3`:

```bash
flex lab3_lexical_analyzer.l
gcc lex.yy.c -o lab3_lexical_analyzer -lfl
./lab3_lexical_analyzer sample_input_3.c
rm lab3_lexical_analyzer lex.yy.c
```

Here, `flex` generates the C file from the `.l` file, `gcc` compiles it into an executable, and then we run the executable with the sample input. Finally, we clean up the generated files.

You can also provide input from keyboard:

```bash
./lab3_lexical_analyzer
```

Then type your input and press `Ctrl+D` to end the input.

remove the executable and generated C file after running to keep the directory clean.

```bash
rm lab3_lexical_analyzer lex.yy.c
```

## Purpose

- Lab Work 1 practices token identification.
- Lab Work 2 practices symbol table design using hashing and chaining.
- Lab Work 3 practices lexical analysis using Flex.

## Author

- Sharif Md. Yousuf

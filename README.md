# CSE 430 Lab Works

This repository contains simple Python implementations for CSE 430 Compiler Design lab tasks.

## Folder Structure

- `Lab Work 1/`
  - `Lab_Work_1.md`
  - `lab1_lexical_analyzer.py`
- `Lab Work 2/`
  - `Lab_Work_2.md`
  - `lab2_symbol_table.py`

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

## Purpose

- Lab Work 1 practices token identification.
- Lab Work 2 practices symbol table design using hashing and chaining.

## Author

- Sharif Md. Yousuf

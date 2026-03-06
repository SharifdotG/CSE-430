# CSE 430: Compiler Design - Lab Work 2

## Introduction

We will build a symbol-table in this assignment. At this initial stage, we will omit many details regarding an actual symbol-table and we will simply adhere to the basic concept that “a symbol-table is an efficient data-dictionary for the symbols used in a program”. Thus, our focus in this assignment is to construct a simple hash-based data-dictionary based on chaining.

Symbol table attributes:

- `NAME`
- `TYPE`
- `SIZE`
- `DIMENSION`
- `Line of Code`
- `Address`

## Inputs

NAME: will be the name of the element
TYPE: will be the type of the element
SIZE: will be the size of the type.
DIMENSION: will be dimension of the type.
Line of Code: will be inserted randomly, you can insert it as you wish.
Address: will be also random, you can insert it as you wish.

The input to your program will be a sequence of six tuples, where each element in each tuple is a string.

## Examples

- `x, ID, 2, 1, 5, 0x0FF`
- `arr, ID, 10, 5, 10, 0x1D3`

The first element of each tuple will be the name of the record to be stored in the symbol table. Hence, you have to apply the hash function on the first element of each tuple that is the name.

## Tasks

- Insert: Insert a new symbol/name along with its type into the symbol table.
- Search: Search for a symbol/name and retrieve its associated type from the symbol table.
- Delete: Remove a symbol/name and its type from the symbol table.
- Show: Display the contents of the symbol table in the console.
- Update: Modify the type or other attributes of an existing entry in the symbol table.

## Implementation Details

To implement the tasks mentioned in the previous section, you need to do the following:

- Declare the following:
  - `struct SymbolInfo`: The definition of this structure will grow gradually throughout the development of this project. For this assignment, we simply need two members, one for storing the symbol (e.g. `x`) and another for storing the type of the symbol (e.g. `IDENTIFIER`).
  - `SymbolInfo *SymbolTable[MAX]`: Since our symbol table will be a hashtable based on chaining, we will have to start with an array of pointers where each pointer points to a list of nodes of type `SymbolInfo`. `SymbolTable` is such an array of pointers. For this assignment, the choice of the size of this array (`MAX`) as well as the hash function is left up to you.
- In addition to this array of pointers, define the following global functions:
  - `insert()`
  - `search()`
  - `delete()`
  - `show()`
  - `update()`
  - `getHashKey()`

## Note

Do not use built-in dict for it in case of python. Built in library for Dict and Linked List can not be used. Please keep this in mind while implementing the symbol table. You have to implement your own data structures for the symbol table.

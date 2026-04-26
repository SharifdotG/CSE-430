# CSE 430: Compiler Design - Lab Work 4: Elimination of Left Recursion in a Grammar

## Introduction

We have already seen what is left recursion in theory class and we know how to eliminate left recursion in a grammar. Whenever there is a production in the form of:

A → A[α1] | A[α2] | β[1] | β[2]

It is considered as left recursion. The elimination rule is:

A → β[1]A' | β[2]A'
A' → α[1]A' | α[2]A' | ε

### Algorithm 1 Elimination of Left Recursion in a Grammar

```pseudocode
Assume the nonterminals are ordered A[1], A[2], A[3], . . . ▷ In the example: S, A, B
for each nonterminal A[i], i = 1 to N do
  for each nonterminal [j], j = 1 to i − 1 do
    Let [j] → β[1] | β[2] | · · · | β[N] be all the rules for [j]
    if there is a rule of the form [i] → [j]α then
      Replace it by [i] → β[1]α | β[2]α | · · · | β[N]α
    end if
  end for
  Eliminate immediate left recursion among the Ai rules
end for
```

Now, use this algorithm to eliminate left recursion from a grammar taken as an input in the console. Follow the theory class lecture slides for more clarification about the topic. You can use any programming language as per your choice.

## Examples

### Example 1

E → E+T | T

After elimination of left recursion, the grammar becomes:

E → TE'
E' → +TE' | ε

Example 2:

T → T∗F | F

After elimination of left recursion, the grammar becomes:

T → FT'
T' → ∗FT' | ε

## Samples: Direct Left Recursion Elimination

### Input

```plaintext
Enter grammar rules (format: A -> Aa | b). Press Enter on empty line to finish:
A -> Aa | Ab | c | d
```

### Output

```plaintext
Original Grammer:
A -> Aa | Ab | c | d

After left recusion elimination:
A -> cA' | dA'
A' -> aA' | bA' | ε
```

*N.B: Completing only the direct part will be enough to get 80% full marks. But if you believe that, you need extra bonus marks, try out the indirect part as well.*

## Samples: Indirect Left Recursion Elimination (BONUS!)

### Input

```plaintext
Enter grammar rules (format: S -> x | y). Press Enter on empty line to finish:
S -> x | y
A -> Sa | Bf | m
B -> Ab | Sc | n
```

### Output

```plaintext
Original Grammar:
S -> x | y
A -> Sa | Bf | m
B -> Ab | Sc | n

Grammar after eliminating left recursion:
S -> x | y
A -> xa | ya | Bf | m
B -> xabB' | yabB' | mbB' | xcB' | ycB' | nB'
B' -> fbB' | ε
```

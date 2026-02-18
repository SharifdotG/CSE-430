'''
CSE 430 - Lab Work 1 🫡
22101128 - Sharif Md. Yousuf

Steps to run the code
1. Put all the files (lab1_lexical_analyzer.py, sample_input_1.c, sample_input_2.c) in a single file
2. `cd` into the folder
3. for sample 1, in the terminal: py lab1_lexical_analyzer.py sample_input_1.c
4. for sample 2, in the terminal: py lab1_lexical_analyzer.py sample_input_2.c
5. You should see the correct output for both the samples :3
'''

import re
import sys


KEYWORDS = {
    "if",
    "else",
    "int",
    "void",
    "float",
    "char",
    "for",
    "while",
    "return",
    "break",
    "continue",
}

PAT = re.compile(
    r"'(?:\\.|[^'\\])'|\d+\.\d+|\d+|>=|<=|==|!=|[><]|[A-Za-z_]\w*|[+\-*/=]|[;:,]|[(){}\[\]]"
)


def remove_comments(s: str) -> str:
    s = re.sub(r"/\*.*?\*/", "", s, flags=re.S)
    return re.sub(r"//.*?$", "", s, flags=re.M)


def analyze(src):
    src = remove_comments(src)
    toks = PAT.findall(src)
    groups = {}
    groups["Keyword"] = set()
    groups["Identifier"] = set()
    groups["Constant"] = set()
    groups["Arithmetic Operator"] = set()
    groups["Logical Operator"] = set()
    groups["Punctuation"] = set()
    groups["Parenthesis"] = set()
    for t in toks:
        if re.fullmatch(r"[A-Za-z_]\w*", t):
            (groups["Keyword" if t in KEYWORDS else "Identifier"]).add(t)
        elif t in "+-*/=":
            groups["Arithmetic Operator"].add(t)
        elif t in (">", "<", ">=", "<=", "==", "!="):
            groups["Logical Operator"].add(t)
        elif t in ";,:":
            groups["Punctuation"].add(t)
        elif t in "(){}[]":
            groups["Parenthesis"].add(t)
        else:
            groups["Constant"].add(t)
    return groups


def print_tokens(tokens):
    order = [
        "Keyword",
        "Identifier",
        "Constant",
        "Arithmetic Operator",
        "Logical Operator",
        "Punctuation",
        "Parenthesis",
    ]
    for k in order:
        v = sorted(tokens[k])
        if v:
            print(f"{k} ({len(v)}): {', '.join(v)}")


def read_input(path):
    if path:
        with open(path, "r") as f:
            return f.read()
    return sys.stdin.read()


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else None
    source_code = read_input(src)
    tokens = analyze(source_code)
    print_tokens(tokens)


if __name__ == "__main__":
    main()

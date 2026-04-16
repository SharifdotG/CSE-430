%{
#include <stdio.h>
#include <string.h>

/* Tracks the current input line number for token reporting. */
int line_no = 1;

/* Checks whether an identifier matches one of the C keywords. */
int is_keyword(const char *word);
extern FILE *yyin;
%}

%option noyywrap

%%
[ \t\r]+                    ; /* Ignore spaces, tabs, and carriage returns. */
\n                          { line_no++; } /* Count each new line. */

"//"[^\n]*                  { printf("%d\t\t%s\t\tcomment\n", line_no, yytext); } /* Match C single-line comments. */

">="|"<="|"=="|"!="|">"|"<" { printf("%d\t\t%s\t\tlogical_op\n", line_no, yytext); } /* Relational and equality operators. */
"="                         { printf("%d\t\t%s\t\tassign_op\n", line_no, yytext); } /* Assignment operator. */

"+"|"-"|"*"|"/"             { printf("%d\t\t%s\t\tarithmetic_op\n", line_no, yytext); } /* Basic arithmetic operators. */

"("|")"|"{"|"}"|"["|"]"     { printf("%d\t\t%s\t\tparenthesis\n", line_no, yytext); } /* Parentheses, braces, and brackets. */
[;:,]                       { printf("%d\t\t%s\t\tpunctuation\n", line_no, yytext); } /* Semicolon, colon, and comma. */

[0-9]+                      { printf("%d\t\t%s\t\tconstant\n", line_no, yytext); } /* Integer constants. */

[A-Za-z_][A-Za-z0-9_]*      {
                                /* Identifiers: start with letter/underscore, then letters/digits/underscore. */
                                /* Decide whether the word is a keyword or identifier. */
                                if (is_keyword(yytext)) {
                                    printf("%d\t\t%s\t\tkeyword\n", line_no, yytext);
                                } else {
                                    printf("%d\t\t%s\t\tidentifier\n", line_no, yytext);
                                }
                            }

.                           ; /* Ignore any unrecognized single character. */
%%

int is_keyword(const char *word)
{
    /* Standard 32 C keywords required in the lab statement. */
    const char *keywords[] = {
        "auto", "break", "case", "char", "const", "continue", "default", "do",
        "double", "else", "enum", "extern", "float", "for", "goto", "if",
        "int", "long", "register", "return", "short", "signed", "sizeof", "static",
        "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"
    };

    int keyword_count = sizeof(keywords) / sizeof(keywords[0]);
    int i;

    for (i = 0; i < keyword_count; i++) {
        if (strcmp(word, keywords[i]) == 0) {
            return 1;
        }
    }

    return 0;
}

int main(int argc, char *argv[])
{
    /* If a file path is provided, read from that file. */
    if (argc > 1) {
        FILE *input_file = fopen(argv[1], "r");

        if (input_file == NULL) {
            perror("Could not open input file");
            return 1;
        }

        yyin = input_file;
        yylex();
        fclose(input_file);
    } else {
        /* Otherwise read directly from keyboard (standard input). */
        yylex();
    }

    return 0;
}

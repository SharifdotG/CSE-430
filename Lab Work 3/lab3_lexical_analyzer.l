%{
#include <stdio.h>
#include <string.h>

int line_no = 1;

int is_keyword(const char *word);
extern FILE *yyin;
%}

%option noyywrap

%%
[ \t\r]+                    ;
\n                          { line_no++; }

"//"[^\n]*                  { printf("%d\t%s\tcomment\n", line_no, yytext); }

">="|"<="|"=="|"!="|">"|"<"  { printf("%d\t%s\tlogical_op\n", line_no, yytext); }
"="                         { printf("%d\t%s\tassign_op\n", line_no, yytext); }

"+"|"-"|"*"|"/"             { printf("%d\t%s\tarithmetic_op\n", line_no, yytext); }

"("|")"|"{"|"}"|"["|"]"     { printf("%d\t%s\tparenthesis\n", line_no, yytext); }
[;:,]                       { printf("%d\t%s\tpunctuation\n", line_no, yytext); }

[0-9]+                      { printf("%d\t%s\tconstant\n", line_no, yytext); }

[A-Za-z_][A-Za-z0-9_]*      {
                                if (is_keyword(yytext)) {
                                    printf("%d\t%s\tkeyword\n", line_no, yytext);
                                } else {
                                    printf("%d\t%s\tidentifier\n", line_no, yytext);
                                }
                            }

.                           ;
%%

int is_keyword(const char *word)
{
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
        yylex();
    }

    return 0;
}

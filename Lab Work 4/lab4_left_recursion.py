def parse_grammar():
    print(
        "Enter grammar rules (format: A -> Aa | b). Press Enter on empty line to finish:"
    )
    grammar = {}
    order = []

    while True:
        line = input().strip()
        if not line:
            break

        lhs, rhs = line.split(" -> ")
        lhs = lhs.strip()
        productions = [p.strip() for p in rhs.split("|")]

        grammar[lhs] = productions
        if lhs not in order:
            order.append(lhs)

    return grammar, order


def starts_with_nt(prod, nt):
    if not prod.startswith(nt):
        return False

    rest = prod[len(nt) :]
    if rest and rest[0] == "'":
        return False
    return True


def eliminate_left_recursion(grammar, order):
    grammar = {k: list(v) for k, v in grammar.items()}
    original_order = list(order)

    for i in range(len(original_order)):
        Ai = original_order[i]

        for j in range(i):
            Aj = original_order[j]
            new_productions = []

            for prod in grammar[Ai]:
                if starts_with_nt(prod, Aj):
                    alpha = prod[len(Aj) :]

                    for aj_prod in grammar[Aj]:
                        new_productions.append(aj_prod + alpha)
                else:
                    new_productions.append(prod)
            grammar[Ai] = new_productions

        left_recursive = []
        non_left_recursive = []
        for prod in grammar[Ai]:
            if starts_with_nt(prod, Ai):
                left_recursive.append(prod[len(Ai) :])
            else:
                non_left_recursive.append(prod)

        if left_recursive:
            Ai_prime = Ai + "'"
            grammar[Ai] = [beta + Ai_prime for beta in non_left_recursive]
            grammar[Ai_prime] = [alpha + Ai_prime for alpha in left_recursive] + ["ε"]

    return grammar


def print_grammar(grammar, order):
    display_order = []
    for nt in order:
        display_order.append(nt)
        nt_prime = nt + "'"
        if nt_prime in grammar:
            display_order.append(nt_prime)

    for nt in grammar:
        if nt not in display_order:
            display_order.append(nt)

    for nt in display_order:
        rhs = " | ".join(grammar[nt])
        print(f"{nt} -> {rhs}")


def main():
    grammar, order = parse_grammar()
    print("\nOriginal Grammar:")
    print_grammar(grammar, order)

    new_grammar = eliminate_left_recursion(grammar, order)
    print("\nGrammar after eliminating left recursion:")
    print_grammar(new_grammar, order)


if __name__ == "__main__":
    main()

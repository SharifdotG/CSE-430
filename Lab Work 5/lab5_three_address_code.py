import ast
import sys


def generate_tac(expression):
    expr = expression.replace("x", "*").replace("–", "-").strip()
    tree = ast.parse(expr, mode="eval")

    tac = []
    temp_idx = [0]

    def get_temp():
        temp_idx[0] += 1
        return f"T{temp_idx[0]}"

    def traverse(node):
        if isinstance(node, ast.Constant):
            return str(node.value)
        if isinstance(node, ast.Name):
            return node.id

        if isinstance(node, ast.BinOp):
            left = traverse(node.left)
            right = traverse(node.right)
            op_map = {
                ast.Add: "+",
                ast.Sub: "-",
                ast.Mult: "x",
                ast.Div: "/",
                ast.Mod: "%",
                ast.Pow: "^",
            }
            op = op_map.get(type(node.op), "?")
            t = get_temp()
            tac.append(f"({len(tac) + 1}) {t} = {left} {op} {right}")
            return t

        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            operand = traverse(node.operand)
            t = get_temp()
            tac.append(f"({len(tac) + 1}) {t} = uminus {operand}")
            return t
        return ""

    traverse(tree.body)
    return tac


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            expr = f.read().strip()
    else:
        expr = input()

    for line in generate_tac(expr):
        print(line)

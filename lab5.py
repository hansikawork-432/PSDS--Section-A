import math

def get_precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def is_operator(c):
    return c in ('+', '-', '*', '/', '^')

def infix_to_postfix(infix):
    op_stack = []
    postfix = []
    i = 0
    n = len(infix)

    while i < n:
        c = infix[i]

        if c.isspace():
            i += 1
            continue

        if c.isalnum():
            operand = ""
            while i < n and infix[i].isalnum():
                operand += infix[i]
                i += 1
            postfix.append(operand)
            continue

        elif c == '(':
            op_stack.append(c)

        elif c == ')':
            while op_stack and op_stack[-1] != '(':
                postfix.append(op_stack.pop())
            if op_stack:
                op_stack.pop()

        elif is_operator(c):
            while (op_stack and 
                   op_stack[-1] != '(' and 
                   get_precedence(op_stack[-1]) >= get_precedence(c)):
                if c == '^' and op_stack[-1] == '^':
                    break
                postfix.append(op_stack.pop())
            op_stack.append(c)

        i += 1

    while op_stack:
        postfix.append(op_stack.pop())

    return " ".join(postfix)

def evaluate_postfix(postfix):
    val_stack = []
    tokens = postfix.split()

    for token in tokens:
        if token.isdigit():
            val_stack.append(int(token))
        elif is_operator(token):
            val2 = val_stack.pop()
            val1 = val_stack.pop()

            if token == '+':
                val_stack.append(val1 + val2)
            elif token == '-':
                val_stack.append(val1 - val2)
            elif token == '*':
                val_stack.append(val1 * val2)
            elif token == '/':
                val_stack.append(int(val1 / val2))
            elif token == '^':
                val_stack.append(int(math.pow(val1, val2)))

    return val_stack[-1]

if __name__ == "__main__":
    symbolic_infix = "A+(B*C)"
    print("Infix (Symbolic):", symbolic_infix)
    print("Postfix Output  :", infix_to_postfix(symbolic_infix))
    print("-" * 42)

    numeric_infix = "5 + ( 3 * 4 ) - 8 / 2"
    postfix_expr = infix_to_postfix(numeric_infix)

    print("Infix (Numeric) :", numeric_infix)
    print("Converted Postfix:", postfix_expr)
    print("Evaluated Result:", evaluate_postfix(postfix_expr))

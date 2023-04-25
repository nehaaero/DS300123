def evaluate_postfix_expression(expression):
    """
    Evaluate a postfix expression using a stack data structure.
    Args:
        expression (str): The postfix expression to be evaluated.
    Returns:
        int/float: The result of the evaluated postfix expression.
    """
    stack = []
    operators = ['+', '-', '*', '/']

    for char in expression:
        if char not in operators:
         
            stack.append(float(char))
        else:
    
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)

    return stack[0]

postfix_expr = "53+62/*35*+"
result = evaluate_postfix_expression(postfix_expr)
print("Postfix Expression:", postfix_expr)
print("Result:", result)
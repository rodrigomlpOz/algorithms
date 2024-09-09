def evaluate(expression):

    intermediate_results = []
    delimiter = ','
    operators = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: x // y
    }

    for token in expression.split(delimiter):
        if token in operators:
            intermediate_results.append(operators[token](
                intermediate_results.pop(), intermediate_results.pop()))
        else:  # token is a number.
            intermediate_results.append(int(token))
    return intermediate_results[-1]

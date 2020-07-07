def function_1():
    return "Output for function 1."


def function_2():
    return "Correct output for function 2."


def function_3(name):
    if type(name) == int:
        return f"x = {name}"
    elif type(name) == float:
        return f"x = {name:.2f}"


def function_4(x, y):
    return float(x) + float(y)


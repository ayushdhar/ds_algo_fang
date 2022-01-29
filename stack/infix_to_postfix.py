def is_operand(s: str):
    return s in ["+", "/", "-", "*"]


def pre(op: str):
    if op in ["+", "-"]:
        return 1
    return 2


def covert():
    pass

class Error(Exception):
    pass

class RULES:
    @staticmethod
    def tasks(tasks: list or tuple):
        if len(tasks) > 5:
            raise Error("Too many problems.")

    @staticmethod
    def operator(operator: str):
        if operator not in ["+", "-"]:
            raise Error("Operator must be '+' or '-'.")

    @staticmethod
    def operand(operand: str):
        if not operand.isdigit():
            raise Error("Numbers must only contain digits.")

        if len(operand) > 4:
            raise Error("Numbers cannot be more than four digits.")


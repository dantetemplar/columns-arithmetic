from base import Task
from typing import Iterable
import re


class RULES:
    @staticmethod
    def search(search):
        if search is None:
            raise Exception("Operator must be '+' or '-'.")
        groups = search.groups()
        RULES.operand(groups[0])
        RULES.operator(groups[1])
        RULES.operand(groups[2])

    @staticmethod
    def problems(problems: list or tuple):
        if len(problems) > 5:
            raise Exception("Too many problems.")

    @staticmethod
    def operator(operator: str):
        if operator not in ["+", "-"]:
            raise Exception("Operator must be '+' or '-'.")

    @staticmethod
    def operand(operand: str):
        if not operand.isdigit():
            raise Exception("Numbers must only contain digits.")

        if len(operand) > 4:
            raise Exception("Numbers cannot be more than four digits.")


def parse(problem: str):
    problem = problem.replace(" ", "")
    search = re.search(r'^(.+)([+-])(.+)$', problem)
    RULES.search(search)
    groups = search.groups()
    operands = int(groups[0]), int(groups[2])
    operator = groups[1]

    return {"operator": operator, "operands": operands}


def arithmetic_arranger(problems: Iterable[str], need_ans: bool = False):
    try:
        RULES.problems(problems)
        tasks = [Task(**parse(problem), need_ans=need_ans)() for problem in problems]
        arranged_problems = ["    ".join(row) for row in zip(*tasks)]

        return "\n".join(arranged_problems if need_ans else arranged_problems[:-1])
    except Exception as error:
        return f"Error: {error.args[0]}"


if __name__ == '__main__':
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

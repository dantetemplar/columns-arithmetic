from typing import Iterable
from functools import reduce


class Task:
    BASE_TYPE = int
    OPERATORS = {"+": BASE_TYPE.__add__,
                 "-": BASE_TYPE.__sub__,
                 # "*": BASE_TYPE.__mul__,
                 # "/": BASE_TYPE.__truediv__,
                 }

    def __init__(self, operands: Iterable[int], operator_symb: str, need_ans: bool = False) -> None:
        self.operands = operands
        self.operator = operator_symb
        self.operator_func = self.OPERATORS[self.operator]
        self.need_ans = need_ans
        self._answer_ = None

    @property
    def answer(self):
        pass

    @answer.getter
    def answer(self):
        if self._answer_ is None:
            self._answer_ = reduce(self.operator_func, self.operands)
        return self._answer_

    def __call__(self):
        l = len(str(max(self.operands))) + 2

        return [str(operand).rjust(l) for operand in self.operands[:-1]] + [
            self.operator + str(self.operands[-1]).rjust(l - 1),
            "-" * l,
            str(self.answer).rjust(l) if self.need_ans else " " * l
        ]

    def __str__(self):
        return "\n".join(self.__call__())

    def __repr__(self):
        return self.__call__()


if __name__ == '__main__':
    task1 = Task([123, 321], "-", need_ans=True)
    task2 = Task([123, 321], "+", need_ans=True)
    task3 = Task([121, 4221], "+", need_ans=True)

    for row in zip(task1(), task2(), task3()):
        print("    ".join(row))
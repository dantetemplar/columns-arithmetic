from unittest import TestCase, main
from base import Task
from arithmetic_arranger import arithmetic_arranger


class BaseTest(TestCase):
    def test_answer_add(self):
        self.assertEqual(Task([123, 4522342], "+").answer, 4522465)

    def test_answer_sub(self):
        self.assertEqual(Task([567567234, 12313523], "-").answer, 555253711)

    def test_str_add(self):
        self.assertEqual(str(Task([23223, 4522], "+")), "  23223\n+  4522\n-------\n       ")

    def test_str_sub(self):
        self.assertEqual(str(Task([54223, 4522], "-")), "  54223\n-  4522\n-------\n       ")


class ArrangerTest(TestCase):
    testcases = {
        'test_two_problems_arrangement1': ((['3801 - 2', '123 + 49'], False),
                                           ('  3801      123\n' +
                                            '-    2    +  49\n' +
                                            '------    -----')),
        'test_two_problems_arrangement2': ((['1 + 2', '1 - 9380'], False),
                                           ('  1         1\n'
                                            '+ 2    - 9380\n'
                                            '---    ------')),
        'test_four_problems_arrangement': ((['3 + 855', '3801 - 2', '45 + 43', '123 + 49'], False),
                                           ('    3      3801      45      123\n' +
                                            '+ 855    -    2    + 43    +  49\n' +
                                            '-----    ------    ----    -----')),
        'test_five_problems_arrangement': ((['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'], False),
                                           ('  11      3801      1      123         1\n' +
                                            '+  4    - 2999    + 2    +  49    - 9380\n' +
                                            '----    ------    ---    -----    ------')),
        'test_two_problems_with_solutions': ((['3 + 855', '988 + 40'], True),
                                             ('    3      988\n' +
                                              '+ 855    +  40\n' +
                                              '-----    -----\n' +
                                              '  858     1028')),
        'test_five_problems_with_solutions': ((['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True),
                                              ('   32         1      45      123      988\n' +
                                               '- 698    - 3801    + 43    +  49    +  40\n' +
                                               '-----    ------    ----    -----    -----\n' +
                                               ' -666     -3800      88      172     1028')),
        'test_too_many_problems': ((['44 + 815', '909 - 2', '45 + 43', '123 + 49',
                                     '888 + 40', '653 + 87'], False),
                                   ('Error: Too many problems.')),
        'test_incorrect_operator': ((['3 / 855', '3801 - 2', '45 + 43', '123 + 49'], False),
                                    ("Error: Operator must be '+' or '-'.")),
        'test_too_many_digits': ((['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'], False),
                                 ("Error: Numbers cannot be more than four digits.")),
        'test_only_digits': ((['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'], False),
                             ("Error: Numbers must only contain digits.")),
    }

    def test_all(self):
        for name, (args, output) in self.testcases.items():
            self.assertEqual(arithmetic_arranger(*args), output)

if __name__ == '__main__':
    main()

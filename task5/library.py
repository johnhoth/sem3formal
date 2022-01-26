# class ElemInitException(Exception):
#     pass
#
#
# class UnknownFormat(ElemInitException):
#     def __init__(self, args):
#         self.message = f"bad args for Elem {args}, only 2 or 4 allowed!"
#         super().__init__(self.message)


class RegularExpressionException(Exception):
    pass


class UnknownSymbol(RegularExpressionException):
    def __init__(self, symbol, index):
        self.message = f"unknown symbol '{symbol}' on position {index}"
        super().__init__(self.message)


class NoOperand(RegularExpressionException):
    def __init__(self, v, stack):
        self.message = f"bad input: lack of operands, there should be {v} more"
        self.message += f". In the end stack is {stack}"
        super().__init__(self.message)


class InapplicableOperator(RegularExpressionException):
    def __init__(self, operator, index):
        self.message = f"inapplicable operator {operator} on position {index}"
        super().__init__(self.message)

INF = 10**9 + 7

class Elem:

    '''
    Elem is class for element of stack
    which is useful for parsing regex in reverse reverse polish notation

    structure of Elem:

    only_x - boolean if the elem contains only x'es

    [x...x][not x][*][not x][x...x]
    [start][     middle    ][ end ]

    begin - number of x'es elem starting with
    middle - max length of string that contains only x'es
    end - number of x'es elem ending with
    '''

    def __init__(self, *args):
        if len(args) == 2: # Elem from x and character
            tmp = self.constructor2(args)
            self.only_x = tmp[0]
            self.begin = tmp[1]
            self.middle = tmp[2]
            self.end = tmp[3]
        # elif len(args) == 4: # Elem just from raw values
        # self.only_x = args[0]
        # self.begin = args[1]
        # self.middle = args[2]
        # self.end = args[3]
        # else:
            # raise UnknownFormat(args)

    def __iter__(self): # to make cast Elem to list possible
        for elem in [self.only_x, self.begin, self.middle, self.end]:
            yield elem

    def constructor2(self, args): # create Elem by x and character
        x, char = args[0], args[1]
        if x == char:
            return [True, 1, 0, 1]
        else:
            return [False, 0, 0, 0]

    def get_result(self):
        return max([self.begin, self.middle, self.end])


def dot(first, second):
    if first.only_x and second.only_x:
        first.begin = first.begin + second.begin
        first.end = first.end + second.begin

    elif first.only_x:
        first.begin = first.begin + second.begin
        first.middle = second.middle
        first.end = second.end
        first.only_x = False

    elif second.only_x:
        first.begin = first.begin
        first.end = first.end + second.begin
        first.only_x = False

    else:
        middle_values = [first.middle,
                        second.middle,
                        first.end + second.begin]
        first.middle = max(middle_values)
        first.end = second.end
        first.only_x = False

    return first

def plus(first, second):
    first.begin = max(first.begin, second.begin)
    first.middle = max(first.middle, second.middle)
    first.end = max(first.end, second.end)

    return first

def star(first):
    if first.only_x and first.get_result() > 0:
        first.middle = INF
    else:
        first.middle = max(first.middle, first.begin + first.end)
    return first

def solve(language, x):
    dp = []
    index = 0
    result = 0
    for c in language:
        if c in 'abc1':
            dp.append(Elem(x, c))
        elif c == '.':
            if len(dp) < 2:
                raise InapplicableOperator(c, index)

            dp[-2] = dot(dp[-2], dp[-1])
            dp.pop()

        elif c == '+':
            if len(dp) < 2:
                raise InapplicableOperator(c, index)

            dp[-2] = plus(dp[-2], dp[-1])
            dp.pop()

        elif c == '*':
            if len(dp) < 1:
                raise InapplicableOperator(c, index)
            dp[-1] = star(dp[-1])

        else:
            raise UnknownSymbol(c, index)

        if dp[-1].get_result() == INF:
            result = 'INF'

        index += 1

    if len(dp) != 1:
        raise NoOperand(len(dp) - 1, [list(elem) for elem in dp])

    if result != 'INF':
        result = dp[-1].get_result()

    return result

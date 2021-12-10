from Stack2 import Stack

class FortranLike:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def fill(self, string):
        symbols = reversed(string.split())
        for each in symbols:
            self.s1.push(each)

    def calculate(self):
        while self.s1.peek():
            symbol = self.s1.pop()
            if symbol.isdigit():
                self.s2.push(int(symbol))
            else:
                x1 = self.s2.pop()
                x2 = self.s2.pop()
                if symbol == '+':
                    self.s2.push(x1 + x2)
                elif symbol == '-':
                    self.s2.push(x1 - x2)
                elif symbol == '/':
                    self.s2.push(x1 / x2)
                elif symbol == '*':
                    self.s2.push(x1 * x2)
                elif symbol == '=':
                    return x1
                else:
                    return 'Wrong symbol!'
        return self.s2.peek()

fl = FortranLike()
fl.fill('1 2 + 3 *')
print(fl.calculate())
f1 = FortranLike()
fl.fill('8 2 + 5 * 9 + =')
print(fl.calculate())

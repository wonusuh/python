class FourCalc:
    def __init__(self, lst):
        self.lst = lst

    def evalExp(self):
        sgn = ""
        total = None
        while self.lst:
            tmp = self.lst.pop(0)
            if tmp == '(':
                tmp = self.evalExp()
            elif tmp == ')':
                break
            try:
                if total == None:
                    raise UnboundLocalError
                val = int(tmp)
                if sgn == "+":
                    total += val
                elif sgn == "-":
                    total -= val
                elif sgn == "*":
                    total *= val
                elif sgn == "/":
                    total /= val
                else:
                    pass
            except UnboundLocalError:
                total = int(tmp)
            except ValueError:
                sgn = tmp
        return total

if __name__ == '__main__':
    lst = ["2", "+", "(", "3", "*", "4", ")"]
    f = FourCalc(lst)
    print(f.evalExp())

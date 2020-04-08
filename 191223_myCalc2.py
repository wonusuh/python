from calcUtil import CalcExp
from fourCalc import FourCalc

def runCalc():
    print("醫낅즺�� 'x'��")
    while True:
        inputStr = input()
        exp = CalcExp(inputStr)
        exp.rmSpace()
        if str(exp) == "x":
            print("怨꾩궛湲곕� 醫낅즺�⑸땲��.")
            return
        exp.rmChars()
        expLst = exp.exp2lst()
        print(expLst)
        result = FourCalc(expLst).evalExp()
        print(result)

runCalc()

def calculating(x):
    sgn = ""
    total = None
    while x:
        tmp = x.pop(0)
        if tmp == "(":
            tmp = calculating(x)
        elif tmp == ")":
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

myList = ["2", "+", "(", "3", "*", "4", ")"]
print(calculating(myList))

class CalcExp:
    EN_NUMSIGN = "1234567890+-*/()"

    def __init__(self, exp):
        self.exp = exp
    
    def rmSpace(self):
        self.exp.strip()
        self.exp = self.exp.replace(" ", "")

    def rmChars(self):
        tmp = ""
        for char in self.exp:
            if self.EN_NUMSIGN.count(char) > 0:
                tmp += char
        self.exp = tmp
    
    def exp2lst(self):
        str = self.exp
        for item in "+-*/()":
            str = str.replace(item, "#%s#" %item)
        tmp = str.split("#")
        for i in range(len(tmp)):
            tmpVal = tmp[i]
            if tmpVal.count("#") > 0:
                tmp[i] = tmp[i].replace("#", "")
        tmp = self.rmEmptyItem(tmp)
        return tmp

    def rmEmptyItem(self, lst):
        tmp = []
        for i in range(len(lst)):
            if lst[i]:
                tmp.append(lst[i])
        return tmp

    def __str__(self):
        return self.exp

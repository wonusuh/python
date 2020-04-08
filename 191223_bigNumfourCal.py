class FourCal:

    def __init__(self): # 생성자 메서드
        self.first = 0
        self.second = 0

    def setdata(self, first, second): # 사칙연산 메서드
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first // self.second
        return result

class BigNum:

    digit = [
        "000000...00...00...000000",
        "....1....1....1....1....1",
        "22222....2222222....22222",
        "33333....333333....333333",
        "4...44...444444....4....4",
        "555555....55555....555555",
        "666666....666666...666666",
        "77777....7....7....7....7",
        "888888...8888888...888888",
        "999999...999999....999999",
        ".......+..+++++..+.......", # 10 +
        "..........-----..........", # 11 -
        "......x.x...x...x.x......", # 12 x
        "......../.../.../........", # 13 /
        ".....=====.....=====.....", # 14 =
        ]

    myBigNum = ""
    def __init__(self, num):
        self.num = num

    def big(self):
        for x in range(5):
            n = []
            for y in range(5):
                n.append(self.digit[self.num][x * 5 + y])
            self.myBigNum += "%s%s%s%s%s\n" %(n[0], n[1], n[2], n[3], n[4])
        print(self.myBigNum)
        return self.myBigNum

# 먼저 객체를 생성하고
a = FourCal()


# 메서드를 사용한다.
a.setdata(2, 3)

print(a.mul())

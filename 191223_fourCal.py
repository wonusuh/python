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
        result = self.first / self.second
        return result

# 먼저 객체를 생성하고
a = FourCal()
b = FourCal()

# 메서드를 사용한다.
a.setdata(2, 3)
b.setdata(4, 5)

print(a.mul(), a.div(), b.mul(), b.div())

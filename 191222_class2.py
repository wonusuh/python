class Ball:
    num = 7
    def changeNum(self, p):
        self.num = p

a = Ball()
print(a.num)
a.num = 9
print(a.num)
a.changeNum(1)
print(a.num)

class RedBall(Ball):
    color = 'red'

b = RedBall()
print(b.num)

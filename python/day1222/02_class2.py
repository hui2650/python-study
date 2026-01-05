print("\n ======= 클래스로 만들기 =======")

class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result
    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(7))
print()
print(cal2.add(9))
print(cal2.add(5))



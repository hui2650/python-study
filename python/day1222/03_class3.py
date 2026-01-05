# 사칙연산 클래스

'''
a = Fourcal()

a.setdata(4, 2)

a.add() >>> 6
a.mul() >>> 8
a.sub() >>> 2
a.div() >>> 2

'''

class FourCal:

    # def __init__(self, first, second):
    #     self.first = first
    #     self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self): 
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


a = FourCal()
print(type(a))

a.setdata(8,2)

print(a.first)
print(a.second)
print()

b = FourCal()
b.setdata(3, 5)
print(b.first)
print(a.first)
print()

print("a.add(): " , a.add())
print("a.mul(): " , a.mul())
print("a.sub(): " , a.sub())
print("a.div(): " , a.div())

c = FourCal()
# print(c.add()) #오류


# __init__이 있을 경우에만
# d = FourCal(4, 3)
# print(d.add())
# print(d.div())

print("\n ====== 클래스 상속 ======\n")

class MoreFourCal(FourCal):

    # # third = 777 # 클래스 변수
    third = 777
    def pow(self):
        result = self.first ** self.second
        return result
    # div 메서드 오버라이딩
    def div(self):
        if self.second == 0: # 나누는 값이 0일 경우 0을 리턴
            return 0
        else:
            return self.first / self.second

e = MoreFourCal()
e.setdata(10,2)
print(e.pow())
print(e.div())

# init 없어서 에러
# f = MoreFourCal(4, 0)
# print(f.add())

g = MoreFourCal()
g.setdata(4, 0)
print(g.third)






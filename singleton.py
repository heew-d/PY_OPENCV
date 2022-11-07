# 싱글턴 패턴

# __new__() : 생성자, init이 불러지기 전에 불러짐. 객체 생성전에 불러짐(class(설계, 구성)이 불러짐))
# __init__() :  생성자, 객체가 가져야할 속성을 만들때 사용(self)

import time

class Foo(object):
    def __new__(cls, *args, **kwargs):
        # print("__new__ is called: cls:", cls) #1

        instance = super().__new__(cls)
        # print('instance: ', instance)

        # instance.bar = 10 # 인스턴스 안에 들어있는 변수 bar 생성
        return instance

    def __init__(self): #self : 객제가 가지고 있는 object 메소드
        # print("__init__ is called self: ", self) #2
        # print("self.bar: ", self.bar)

        pass

# ins = object.__new__(Class)
# object.__init__(ins)

s = Foo()
print(s) #3


# 클래스 변수, 객체 변수

class ClassVar():
    foo = 'foo'
    pass

#인스턴스, 객체 x, 클래스 o
print('ClassVar.foo: ', ClassVar.foo)

ClassVar.foo = 'foo2'
print('ClassVar.foo: ', ClassVar.foo)

cv = ClassVar()
print('cv.foo: ', cv.foo)

# id 주소가 똑같다!! 같은 메모리 공간을 공유한다
print(f'ClassVar.foo: {id(ClassVar.foo)}, cv.foo: {id(cv.foo)}')


# 클래스 메서드
class ClassMethod():
    
    count = 100
    _protectVar = 'protect'
    __privateVar = 'private'

    @classmethod
    def print_count(cls):
        print('print_count: ', cls.count)
        print('print_count _protectVar: ', cls._protectVar)
        print('print_count __privateVar: ', cls.__privateVar) # 접근 가능
    pass

ClassMethod.print_count()
# ClassMethod.__privateVar # 접근 불가능


class Singleton(object):
    def __new__(cls, *args, **kwargs):

        # 속성이 존재할때는 이미 존재하는 속성을 리턴
        if hasattr(cls, "_instance"):
            return cls._instance

        # 클래스, 인스턴스(사례), 객체(오브젝트)

        # obj = Class()

        # cls (클래스 설계)를 토대로 인스턴스 생성
        cls._instance = super().__new__(cls) # 클래스의 변수 생성
        return cls._instance 
    
    def __init__(self):
        # self.figures = []
        pass

    # def figure(self):
    #     fig = time.time()
    #     self.figures.append(fig)

    #     return fig

    # def getFigures(self):
    #     return self.figures

    @classmethod
    def figure(cls):
        fig = time.time()
        cls().figures.append(fig)
        return fig
    
    @classmethod
    def figureClear(cls):
        cls().figures.clear()
        return cls().figures

    @classmethod
    def staticMethod(a,b):
        print('total: ', a+b)
        # Singleton()

s1 = Singleton()
s2 = Singleton()

# Singleton.staticMethod()

# print('s1: ', s1)
# print('s2: ', s2)

# s1Figure = s1.figure()
# s2Figure = s2.figure()

# print('s1 figure: ', s1.getFigures())
# print('s2 figure: ', s2.getFigures())

fig1 = Singleton.figure()
time.sleep(3)
fig2 = Singleton.figure()

print('fig1: ', fig1)
print('fig2: ', fig2)

print('s1 figure: ', s1.figures)
print('s2 figure: ', s2.figures)

figures = Singleton.figureClear()

print('figures: ', figures)
print('s1 figure: ', s1.figures)
print('s2 figure: ', s2.figures)
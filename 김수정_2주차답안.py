import re
#1번
#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)

#2번
class Developer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def getSalary(self, day):
        print("{0} 월급 : {1:,}" .format(self.name, day * 100000))

#3번
class WebDeveloper(Developer):
    def __init__(self, id, name):
        Developer.__init__(self, id, name)
    
    def getSalary(self, day):
        print("{0} 월급 : {1:,}" .format(self.name, day * 200000))

#인스턴스 생성
d = Developer(1, "개발자")
d.getSalary(5)

wd = WebDeveloper(2, "웹 개발자")
wd.getSalary(5)

#4번
"""
함수 : 한 가지 기능을 수행
클래스 : 함수와 속성(변수) n개를 포함
모듈 : 함수나 변수 또는 클래스를 모아 놓은 파일
패키지 : 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있도록 하는 것. 모듈과 디렉터리로 이루어져있음
"""

#5번
postCheck = re.compile("(\d{3})-(\d{2})")
print(bool(postCheck.match("123-45")))
print(bool(postCheck.match("가나다-12")))
# class1.py
#클래스 정의
class Person:
    #클래스에 소속된 멤버변수(주로 데이터를 공유) static키워드 추가
    num_person = 0
    def __init__(self):
        #인스턴스 멤버 변수는 여기에서 초기화
        self.name = "default name"
        Person.num_person += 1
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성
p1 = Person()
p2 = Person()
p3 = Person()
print("인스턴스 갯수:{0}".format(Person.num_person))

#런타임시에 멤버 변수 추가(동적 언어는 가능)
Person.title = "new title"
print(Person.title)
print(p1.title)
print(p2.title)
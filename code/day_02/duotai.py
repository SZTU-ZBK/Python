#多态：传入不同的实例对象，产生不同的结果
class Dog(object):
    def work(self):
        print('Working')
class ArmyDog(Dog):
    def work(self):
        print('追击敌人！！！')
class DrugDog(Dog):
    def work(self):
        print('追查毒品！！！')
class Person(object):
    def work(self,dog):
        dog.work()
drug = DrugDog()
person =Person()
person.work(drug)

class Dog(object):
    __tooth = 10

    @classmethod                #����Ҫ�������˽������ʱ�������෽�����з���
    def get_tooth(cls):         #�෽��һ������������ʹ�ã����Խ�ʡ�ڴ�
        return cls.__tooth
dog_1 = Dog()
print(dog_1.get_tooth())
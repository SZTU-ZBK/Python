class A():                   #Ĭ�ϼ̳�object��һ������߽Ƕ����࣬���������������
    def __init__(self):
        self.a = 'a'
    def PrintInfo(self):
        print(self.a)
class B(A):                   #����Ĭ�ϼ̳и�����������Ժͷ���
    pass
test = B()
test.PrintInfo()
        
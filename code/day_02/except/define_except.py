#自定义异常类
class DefineExcept(Exception):
    def __init__(self,length,minlen):
        self.length = length
        self.minilen = minlen
    def __str__(self):
        if self.length<self.minilen:
            return '密码长度太小'
try:
    password = [1,2]
    if len(password)<4:
        raise DefineExcept(len(password),4)        #raise用于抛出异常类创建的对象
except Exception as result:
    print(result)
else:
    print('程序执行成功！！！')
finally:
    print('程序结束！！！')

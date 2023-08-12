#import 模块名
#from 模块名 import 功能名
#from 模块名 import *    从某个模块中导入所有代码，可以直接调用功能，不需要 模块.功能进行调用
#import 模块名 as 别名
#from 模块名 import 功能名 as 别名
#变量名不可跟包名相同，否则会被覆盖
__all__ = ['add_test']          #只有在all列表内的函数才会被from module import * 导入，但是import module不受影响，包->module->功能（函数）
def add_test(a,b):
    print(a+b)
    return a+b
def add_test_b(a,b):
    print(a+b)
    return a+b
if __name__ == '__main__':
    add_test(3,3)
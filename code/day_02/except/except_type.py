#异常类型：NameError(未定义的变量名）、ZeroDivisionError(除0)
try:
    print(num)
except (NameError,ZeroDivisionError) as result:          #捕获多个异常可以通过元组进行拼接，result是改代码对应的异常信息
    print(result)
try:
    print(1/0)
except Exception as result:                              #Exception是所有异常的父类，这样写可以捕获所有异常
    print(result)


try:
    print(num)                                           
except NameError as result:          
    print(result)
else:                                                    #else表示如果代码没有异常，将会执行else块内的代码
    num=num+1
    print(num)

try:
    print(num)       
    #如果try之后报错的话，会直接跳到except,try接下去的代码不会被执行                                  
except NameError as result:          
    print(result)
else:                                                    #else表示如果代码没有异常，将会执行else块内的代码
    num=num+1
    print(num)
finally:                                                 #finall:无论是否异常，都要执行的代码
    print('最后必须执行的代码')
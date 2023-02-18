# #   数据类型得相互转换 


# #python提供了一些内置得函数可以让我们实现诗句自建得转换


# a = int("100")  #字符串转数字
# b = str(100)   #数字转为字符串
# c = list((1,2,3))   #元组转为数组
# d = tuple([1,2,3])  #数组转为元组 
# e = 



# #type获取元素得数据类型
# print(type(a),a)
# print(type(a),a)
# print(type(a),a)
# print(type(a),a)
# print(type(a),a)



#根据数据得类型来动态转换；去掉引号
e1 = eval = ('(1,2,3)')
e2 = eval = ("(1)")
e3 = eval = ("[1,2,3]")
e4 = eval = ('{"1","2","3"}')
e5 = eval = ('e1')   #字符串变量
#ebal = ("e6")   #e6变量没有在之前代码定义，所以会报错

print (type(e1),type(e2),type(e3),type(e4),e5)
eval


#python得代码执行顺序
#从上往下，从左往右，从里到外


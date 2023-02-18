#python得语句
#赋值语句
#判断语句 if/elif/else判断语句
# a =int(input("请输入你的年龄："))
# if a > 18:
#     print("成年了")
# elif a > 10:    #如果A得值小于或者等于并且A > 10 (10.18)
#     print("未成年")
# elif a > 5:
#     print("奶娃娃")
# else:
#     print("花一样得年纪")



#如果if满足条件去执行pritn  如果不满足if 继续执行下面得elif




#示范if else
a = 9
b = 9
if  a < 10:
    print("大于十")
    if b < 5:
        print("大儿子")
    else:
        if b > 10:
            print("等待")
        else:
            print("小于大大")
else:
    print("大大大")


#if的条件
# >  :数字比较，a > b 如果a大于b条件成立
# <：数字比较
# >=：数字比较
# <=：数字比较
# ==；两个值是否相等，int/str/tuple/list/dict
# !=：两个值不相等，int/str/tuple/list/dict
# in:   判断一个值是否包含在另外一个值中
# not in：判断一个值是否包含在另外一个值中
# is ：
# is not ：

#in和notin的用法
a = "大"
b = "大蟒蛇"
if a in b :
    print("好大一个蟒蛇")

else:
    print("好小一个蟒蛇")


a = "大"
b = "大蟒蛇"
if a not in b :
    print("好大一个蟒蛇")

else:
    print("好小一个蟒蛇")



#is  is  not 的用法
if "好大" is True:  #类型和值是否一致   0假1真
    print("顶顶顶顶")
else:
    print("卡布角落")


if "好大" is   not  True:  #类型和值是否一致
    print("顶顶顶顶")
else:
    print("卡布角落")


# 循环语句for/while
#遍历：字符串，数组，元组，字典：
z = "只是来之上海的10K工资"
for i in z:  #取值
    print(i)
b = ["4","5","6","5","大大大大大大大"]    
m = ("4","5","6","5","大大大大大大大")
for i in b:
    print(i)


#字典遍历
a = {"字典":"大字典","小指点":"ddd"}
for v in a:
    print(v,a[v])  #a["字典"]  v="字典" >  a[v]  


#range:序列生成器：快速生成一个数值
range(10)  #[0123456798]

for jj in range(10):
    print(jj)


#range (开始值，结束值，步长)到结束值，不包含结束值


for jj in range(2,11,2):  #会取值2 4 6 8 10    前面一个数字是  从第几位数字开始  中间数字11  代表总共取值   最后一位2 代表，每取值一次，跳过两位数值 
    print(jj)

import pymysql #导入的方式是固定的



# def query(sql):
# #操作深数据库的句柄：类似于ncicat的操作
# db = pymysql.connect(host='119.45.233.102',port=3306,user='testgoup',passwd='1qaz!QAZ',db='tsetdb')  #这是第一步连接数据库
# #获取游标     获取查询的窗口
# cur = db.cursor()  #
# sql = "select * from t_user where id = 1"  #sql语句不用写分号，写上也行
# cur.execute(sql)      #执行SQL查询语句
# res = cur.fetchall()   #获取sql执行的查询结果
# db.close                  #关闭数据连接，类似于exit()



def query(sql):


    DBCONFIG = {"h's"}


    #操作深数据库的句柄：类似于ncicat的操作
    db = pymysql.connect(**DBCONFIG)  #这是第一步连接数据库
    #获取游标     获取查询的窗口
    cur = db.cursor()  #
    sql = "select * from t_user where id = 1"  #sql语句不用写分号，写上也行
    cur.execute(sql)      #执行SQL查询语句
    res = cur.fetchall()   #获取sql执行的查询结果
    db.close                  #关闭数据连接，类似于exit()
    return res












sql = "select * from t_user where id = 1"  #sql语句不用写分号，写上也行
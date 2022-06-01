 # -*- coding: UTF-8 -*-
import sqlite3


#一、连接数据库
# conn=sqlite3.connect("test.db")
# print("打开成功")

# # 二、创建数据表
 # # conn=sqlite3.connect("test.db")
 # # print("打开成功")
 # # c=conn.cursor()     #获取游标
 # # sql='''
 # #     create table shujuku
 # #         (id int primary key not null auto,
 # #         name text not null,
 # #         age int not null,
 # #         address char(50),
 # #         salary real);
 # # '''
 # # c.execute(sql)
 # # conn.commit()
 # # conn.close()
 # # print("建表成功")


#3、插入数据
conn=sqlite3.connect("test.db")
print("打开成功")
c=conn.cursor()     #获取游标
# sql1='''
# insert into shujuku (id,name,age,address,salary)
# values(1,"吴渊",24,"武汉",12000);
# '''
# sql2='''
# insert into shujuku (id,name,age,address,salary)
# values(2,"万嘉琦",23,"武汉",8000);
# '''
# c.execute(sql1)
# c.execute(sql2)
# conn.commit()
# conn.close()
#4、查询数据


conn=sqlite3.connect("test.db")
print("打开成功")
c=conn.cursor()     #获取游标
sql="select id,name,address,salary from shujuku"
# c.execute(sql1)
cursor=c.execute(sql)

for row in cursor:
    print("id=",row[0])
    print("name=",row[1])
    print("address", row[2])
    print("salary", row[3],"\n")

conn.close
print("数据查询完毕")

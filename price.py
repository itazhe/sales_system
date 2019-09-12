#!/usr/bin/python3
# -*- coding: utf-8 -*-

user_name = input("请输入工号：")

# 普通收银员
if user_name == "yrz123":
    print('''
    1. 收银
    2.退货退款
    3.商品报废
    ''')
    n = int(input("请输入要执行的序号："))
    while True:
        if n < 1 or n > 3:
            print("序号输入有误，请重新输入！")
            n = int(input("请再输入要执行的序号："))
        else:
            break

# 老板
elif user_name == "azhe666":
    print('''
    1. 收银
    2.退货退款
    3.商品报废
    4.库存
    5.销售额
    ''')
    n = int(input("请输入要执行的序号："))
    while True:
        if n < 1 or n > 5:
            print("序号输入有误，请重新输入！")
            n = int(input("请再输入要执行的序号："))
        else:
            break

# 收银
if n == 1:
    print(
    '''
                           a z h e 收 银 系 统
    *********************************************************************
        条码                    商品名称            单价            数量
       10001                  飘柔洗发水           35.0              10
       10002                海飞丝洗发水           42.0              17
       10003              霸王防脱洗发水           65.0              34
    *********************************************************************

    ''')
    goods_number = int(input("请输入商品序列号："))
    print("代码生成中")
    # # 执行SQL语句 提取商品的详细信息
    # cur.execute("select * from goods where number=%s" % goods_number)
    # # 通过游标获取执行结果 此处获取所有行
    # rows1 = cur.fetchall()
    # # 执行SQL语句 提取商品的价格
    # cur.execute("select price from goods where number=%s" % goods_number)
    # # 通过游标获取执行结果 此处获取所有行
    # rows2 = cur.fetchall()
    # # 输出商品的详细信息
    # print(rows1)
    # # 输出商品总计价格
    # print("总计: " + str(rows2) + "元")

# 退货退款
if n == 2:
    goods_number = int(input("请输入退货商品序列号："))
    print("代码生成中")
    '''
    需要考虑购买客户的用户信息及曾购买商品信息，更完善的话加上时间
    '''

# 商品报废
if n == 3:
    goods_number = int(input("请输入报废商品序列号："))
    print("代码生成中")
    '''
    数据库指定商品的数量-1，报废的商品用一张表列出，并计算出其总价格
    '''

# 库存
if n == 4:
    print("代码生成中")
    '''
    库存，列出商品的序列号，名称，数量，当数量小于一定数值时，在下面单独显示出来 
    或者直接将小于一定数值的商品输出
    '''

# 销售额
if n == 5:
    print("代码生成中")
    '''
    统计所有商品销售的数量和价格，并计算其总额
   
    '''



#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import user_reg_login

conn = pymysql.connect("127.0.0.1", "azhe", "602661651nizhan$", "prdb")
# 获取一个游标对象(Cursor类)，用于执行SQL语句
cur = conn.cursor()


def goods_list():
    '''
    函数内容：商品列表
    '''
    
    # 执行任意支持的SQL语句
    cur.execute("select * from goods")
    # 通过游标获取执行结果
    rows = cur.fetchall()
    print("#" * 70)
    print("%s%13s%20s%10s%10s" % ("ID", "条码", "商品名称", "单价","数量"))

    n = 0
    while n < len(rows):
        ID = rows[n][0]
        barcode = rows[n][1]
        pname = rows[n][2]
        price = rows[n][3]
        pnumber = rows[n][4]
            
        print("%s%15s%17s%12s%12s" % (ID, barcode, pname, price, pnumber))
        n += 1
    print("#" * 70)


list1 = []
list2 = []
sum = 0
m = 0
def shopping_cart(num2):
    '''
    函数内容：购物车
    '''
    global sum
    global m


    cur.execute("select * from goods where barcode=%s", goods_barcode)
    rows = cur.fetchall()
    print("=" * 75)
    print("%s%13s%20s%10s%10s%10s" % ("ID", "条码", "商品名称", "单价", "数量", "小计"))
    print("-" * 75)
    if num2 == 1:
        # 购物车
        list1.append(list(rows[0]))
 
        while True:
            ID = list1[m][0]
            barcode = list1[m][1]
            pname = list1[m][2]
            price = list1[m][3]
            sub = float(price) * goods_number

            list2.append("%s%15s%17s%12s%12s%12s" % (ID, barcode, pname, price, goods_number, sub))
            m += 1
            break

        n = 0
        while n < len(list2):
            print(list2[n])
            n += 1
        sum += sub 
    elif num2 == 2:
        # 结算 购物车列表
        n = 0
        while n < len(list2):
            print(list2[n])
            n += 1
    elif num2 ==3:
        # 删除购物车中指定商品
        n = 0
        while n < len(list2):
            if list2[n][:4] == goods_del:
                list2.remove(list2[n])
            # print(list2[n])
            try:
                print(list2[n])
            except:
                pass
            n += 1
        n = 0
        sum = 0
        while n < len(list2):
            x = list2[n].split(" ")[-1]
            sum += float(x)
            n += 1

    print("-" * 75)
    print(" " * 67 + "总计：%s" % sum)
    print("=" * 75)
    

def system_main():
    '''
    函数内容：销售系统主函数
    '''
    global goods_barcode
    global goods_number
    global goods_del
    goods_list()

    while True:
        print('''购物车操作指令：
        添加商品(a)   修改(e)   删除(d)   结算(p)   后台管理(r)
        ''')
        n = input(">")
        if n == "a":
            goods_barcode = int(input("请输入商品的条码："))
            goods_number = int(input("请输入购买数量："))
            shopping_cart(1)
        elif n == "e":
            goods_ID = int(input("请输入需要修改的商品ID："))
            goods_number2 = int(input("请输入新的购买数量："))
            # shopping_cart(1, goods_number2)
        elif n == "d":
            goods_del = input("请输入要删除的商品ID：")
            shopping_cart(3)
        elif n == "p":
            shopping_cart(2)
            print("欢迎下次光临!!!")
            break
        elif n == "r":
            goods_list()  
            print('''欢迎进入超市后台管理平台
后台操作指令：
    添加商品(a)  修改商品(e)  删除商品(d)  退出(q)
            ''')
            n = input(">")
            if n == "a":
                goods_barcode = int(input("请输入商品的条码："))
                goods_name = input("请输入商品名称：")
                goods_price = input("请输入商品单价：")
                goods_number = input("请输入商品数量：")
                if user_reg_login.goods_infor(goods_barcode, goods_name, goods_price, goods_number):
                    print("商品添加成功")
                else:
                    print("商品添加失败")
        else:
            print("请输入正确的操作指令")


def user_login():
    '''
    函数内容：用户登录
    '''
    myuname = input("请输入用户名：")
    mypasswd = input("请输入密码: ")
    if user_reg_login.check_uname_pwd(myuname, mypasswd):
        print("登录失败")
        
    else:
        print("登录成功")
        system_main()


def user_reg():
    '''
    函数内容：用户注册
    '''
    myuname = input("请输入用户名：")
    mypasswd = input("请输入密码：")
    myphone = input("请输入手机号：")
    myemail = input("请输入邮箱：")
    if not user_reg_login.user_reg(myuname, mypasswd, myphone, myemail):
        print("注册失败！")
    else:
        print("用户%s注册成功！" % myuname)

print(
'''
欢迎登录azhe销售系统！！！
1. 登 录
2. 注 册
'''
)
num1 = int(input("请输入操作序号>"))
if num1 == 1:
    user_login()
elif num1 == 2:
    user_reg()







# user_name = input("请输入工号：")

# 普通收银员
# if user_name == "yrz123":
    # print('''
    # 1. 收银
    # 2.退货退款
    # 3.商品报废
    # ''')
    # n = int(input("请输入要执行的序号："))
    # while True:
    #     if n < 1 or n > 3:
    #         print("序号输入有误，请重新输入！")
    #         n = int(input("请再输入要执行的序号："))
    #     else:
    #         break
#     while True:
#         print(
#         '''
#                             商   品  清  单
#         *********************************************************************
#             条码                    商品名称            单价            数量
#         10001                  飘柔洗发水           35.0              10
#         10002                海飞丝洗发水           42.0              17
#         10003              霸王防脱洗发水           65.0              34
#         *********************************************************************
#         用户操作指令：
#             添加商品(a)   修改(e)   删除(d)   结算(p)
#         ''')
#         n = input(">")
#         if n == "a":
#             goods_barcode = int(input("请输入商品的条码："))
#             goods_number = int(input("请输入购买数量："))
#         if n == "e":
#             goods_ID = int(input("请输入需要修改的商品ID："))
#             goods_number = int(input("请输入新的购买数量："))
#         if n == "d":
#             goods_del = int(input("请输入要删除的商品ID："))
#         if n == "p":
#             print("欢迎下次光临")
#             break


# # 老板
# elif user_name == "azhe666":
#     while True:
#         print(
#         '''
#                             商   品  清  单
#         *********************************************************************
#             条码                    商品名称            单价            数量
#         10001                  飘柔洗发水           35.0              10
#         10002                海飞丝洗发水           42.0              17
#         10003              霸王防脱洗发水           65.0              34
#         *********************************************************************
#         用户操作指令：
#             添加商品(a)   修改(e)   删除(d)   结算(p)   后台管理(r)
#         ''')
#         n = input(">")
#         if n == "a":
#             goods_barcode = int(input("请输入商品的条码："))
#             goods_number = int(input("请输入购买数量："))
#         if n == "e":
#             goods_ID = int(input("请输入需要修改的商品ID："))
#             goods_number = int(input("请输入新的购买数量："))
#         if n == "d":
#             goods_del = int(input("请输入要删除的商品ID："))
#         if n == "p":
#             print("欢迎下次光临")
#             break
#         if n == "r":
#             print(
#             '''
#                                 商   品  清  单
#             *********************************************************************
#                 条码                    商品名称            单价            数量
#             10001                  飘柔洗发水           35.0              10
#             10002                海飞丝洗发水           42.0              17
#             10003              霸王防脱洗发水           65.0              34
#             *********************************************************************
#             欢迎进入超市后台管理平台
#             后台操作指令：
#                 添加商品(a)  修改商品(e)  删除商品(d)  退出(q)
#             ''')
#             n = input(">")

#####################################################################################3

    # print('''
    # 1. 收银
    # 2.退货退款
    # 3.商品报废
    # 4.库存
    # 5.销售额
    # ''')
    # n = int(input("请输入要执行的序号："))
    # while True:
    #     if n < 1 or n > 5:
    #         print("序号输入有误，请重新输入！")
    #         n = int(input("请再输入要执行的序号："))
    #     else:
    #         break



# 收银
# if n == 1:
    


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

# # 退货退款
# if n == 2:
#     goods_number = int(input("请输入退货商品序列号："))
#     print("代码生成中")
#     '''
#     需要考虑购买客户的用户信息及曾购买商品信息，更完善的话加上时间
#     '''

# # 商品报废
# if n == 3:
#     goods_number = int(input("请输入报废商品序列号："))
#     print("代码生成中")
#     '''
#     数据库指定商品的数量-1，报废的商品用一张表列出，并计算出其总价格
#     '''

# # 库存
# if n == 4:
#     print("代码生成中")
#     '''
#     库存，列出商品的序列号，名称，数量，当数量小于一定数值时，在下面单独显示出来 
#     或者直接将小于一定数值的商品输出
#     '''

# # 销售额
# if n == 5:
#     print("代码生成中")
#     '''
#     统计所有商品销售的数量和价格，并计算其总额
   
#     '''



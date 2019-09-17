#!/usr/bin/python3
# -*- coding: utf-8 -*-


import user_reg_login

def system_main():
    '''
    函数内容：销售系统主函数
    '''
    while True:
        print(
        '''
        购物车操作指令：
            添加商品(a)   修改(e)   删除(d)   结算(p)   后台管理(r)
        ''')
        n = input(">")
        if n == "a":
            goods_barcode = int(input("请输入商品的条码："))
            goods_number = int(input("请输入购买数量："))
        if n == "e":
            goods_ID = int(input("请输入需要修改的商品ID："))
            goods_number = int(input("请输入新的购买数量："))
        if n == "d":
            goods_del = int(input("请输入要删除的商品ID："))
        if n == "p":
            print("欢迎下次光临")
            break
        if n == "r":
            print(
            '''
            欢迎进入超市后台管理平台
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



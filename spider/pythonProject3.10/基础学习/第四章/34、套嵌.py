# answer=input("大宝儿玩英雄联盟吗？")
#
# if answer=="玩":
#     honer = input("大宝儿的段位多少？")
#     if honer =="最强王者":
#         print("世界冠军一半是你操练出来的")
#     else:
#         if honer=="超凡大师":
#             print("下一个世界冠军就在我家")
#         else:
#             if honer=="璀璨钻石":
#                 print("我家大宝儿无人能挡")
#             else:
#                 if honer=="流光翡翠":
#                     print("我家大宝儿神挡杀神")
#                 else:
#                     if honer=="华贵铂金":
#                         print("天天带吴渊子躺赢")
#                     else:
#                         print("吴渊子你打输出使点劲")
#
# else:
#     print("好的谢谢！")
answer=input("您好，请问您有会员卡吗？")
if answer =="有":
    num=float(input("好的，我们讲对您进行积分和打折，请输入购物金额："))
    if num>=200:
        print("打8折，付款金额为：",num*0.7)
    else:
        if num>=100 and num<200:
            print("打8折，付款金额为：",num*0.8)
        else:
            if num>=50 and num<100:
                print("打9折，付款金额为：",num*0.9)
            else:
                print("不打折，付款金额为：",num)
else:
    #if answer=="没有":
    ask =input("您想办一张会员卡吗？")
    if ask =="可以":
        print("好的，请支付5元手续费。")
        num = float(input("好的，我们讲对您进行积分和打折，请输入购物金额："))
        if num >= 200:
            print("打8折，付款金额为：", num * 0.7)
        else:
            if num >= 100 and num < 200:
                print("打8折，付款金额为：", num * 0.8)
            else:
                if num >= 50 and num < 100:
                    print("打9折，付款金额为：", num * 0.9)
                else:
                    print("不打折，付款金额为：", num)
    else:
        num = float(input("好的，请输入购物金额："))
        if num>=300:
            print("打9折，请支付：",num*0.9)
        else:
            print("不打折，支付金额为：",num)
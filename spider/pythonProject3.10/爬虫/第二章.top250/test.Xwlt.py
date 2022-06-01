# -*- coding: UTF-8 -*-
import xlwt
workbook=xlwt.Workbook(encoding="utf-8")   #数据保存到硬盘，保存的对象为workbook
worksheet=workbook.add_sheet("sheet1")     #创建工作表
worksheet.write(0,0,"yezi")
workbook.save("yezi.xls")




#将乘法口诀表保存至Excel
workbook=xlwt.Workbook(encoding="utf-8")   #数据保存到硬盘，保存的对象为workbook
worksheet=workbook.add_sheet("sheet1")

for i in range(1,10):
    for n in range(1,i+1):
        worksheet.write(i-1,n-1, "%d*%d=%d"%(i,n,i*n))
workbook.save("9*9口诀表.xls")
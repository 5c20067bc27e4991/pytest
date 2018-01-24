# -*- coding: utf-8 -*-
'''
Created on 2017年3月21日
@author: guanglin
'''
import xlsxwriter
wb=xlsxwriter.Workbook('test.xlsx')
ws=wb.add_worksheet('sheet1')
ws.set_column('A:A', 20)
ws.write('A1', 'hello')
ws.write(1,0,'world')
wb.close()
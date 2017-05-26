# coding=utf-8
import xlrd,xlwt
from xlutils.filter import process,XLRDReader,XLWTWriter
#from xlutils.copy import copy
from time import strftime,localtime,time
class GetIp:
	def __init__(self):
		""" 
		Constructor 
		"""
		self.times_write_wt = 0
	def copy2(self,wb):
		w = XLWTWriter()
		process(XLRDReader(wb,'unknown.xls'),w)
		return w.output[0][1], w.style_list

	def update_content(self, path_excel):
		self.path_excel=path_excel
		rdbook = xlrd.open_workbook(self.path_excel, formatting_info=True)
		sheetx= 0
		rdsheet = rdbook.sheet_by_index(sheetx)
		wtbook, style_list = self.copy2(rdbook)
		wtsheet = wtbook.get_sheet(sheetx)
		style = xlwt.easyxf('align: wrap on')
		nrow =1
		ncol = 7
		get_list_ip=[]
		get_list_longday = []
		get_list_nowday=[]
		self.rows= rdsheet.nrows
		#print  rows
		for row_o  in range(1,self.rows):
			cell_ip = rdsheet.cell(row_o,ncol).value
			get_list_ip.append(cell_ip)
		#获取无故障最长时间列表
		for day_o in range(1, self.rows):
			cell_day = rdsheet.cell(day_o, ncol+1).value
			get_list_longday.append(cell_day)
		#获取当前运行天数列表
		for now_day_o in range(1, self.rows):
			cell_day_now = rdsheet.cell(now_day_o, ncol+2).value
			get_list_nowday.append(cell_day_now)
	#wtbook.close()
		print get_list_ip
		return get_list_ip,get_list_longday,get_list_nowday

	def write_excel(self,sour_path,dst_path,long_day,now_day,now_date,now_starus,ip_last,text_all):
		self.sour_path = sour_path
		self.long_day=long_day
		self.now_day=now_day
		self.now_date=now_date


		rdbook = xlrd.open_workbook(self.sour_path, formatting_info=True)
		sheetx_wt = 0
		rdsheet_wt = rdbook.sheet_by_index(sheetx_wt)
		wtbook, style_list = self.copy2(rdbook)
		wtsheet_wt = wtbook.get_sheet(sheetx_wt)
		style = xlwt.easyxf('align: wrap on')
		nrow = 1
		ncol_long_day = 8
		ncol_now_day=9
		ncol_now_date=11
		ncol_now_status =12

		get_list_longday = []
		self.rows_wt=rdsheet_wt.nrows
		long_len=range(len(self.long_day))
		now_len = range(len(self.now_day))
		date_len= range(len(self.now_date))
		try:
			for i in long_len:
				xf_index=rdsheet_wt.cell_xf_index(nrow,ncol_long_day)
				#写最长老化天数
				wtsheet_wt.write(nrow,ncol_long_day,self.long_day[i],style_list[xf_index])
				#写当前老化天数
				wtsheet_wt.write(nrow,ncol_now_day,self.now_day[i],style_list[xf_index])
				#写当前日期
				wtsheet_wt.write(nrow,ncol_now_date,self.now_date,style_list[xf_index])
				#写当前状态
				wtsheet_wt.write(nrow, ncol_now_status, now_starus, style_list[xf_index])
				#把从设备读取的内容写入到以设备ip最后三位结尾的sheet页中
				ws=wtbook.add_sheet(ip_last[i],cell_overwrite_ok=True)
				ws.col(1).width = 20000
				ws.write(1,1,text_all[i],style)
			#print '当前状态是：',now_starus.encode('utf-8')
			#now_starus
				nrow+=1
				print 'write is ok!',nrow
			today_t=strftime('%y%m%d%H',localtime(time()))
			wtbook.save(dst_path+'/'+today_t+'.xls')
		except Exception,f:
			print Exception, ":", f
			print u'Excel 写入存在问题，请确认源文件未打开，目标文件已关闭。'


#if __name__ == '__main__':
	#getips=GetIp()
	#getips.update_content('c:/Users/Administrator/Documents/test/changqilaohua-input/new.xls')
	#pass
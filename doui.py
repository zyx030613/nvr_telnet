# -*- coding: utf-8 -*-

""" 
Module implementing Dialog. 
"""


import telnetlib
import re
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QMessageBox
from PyQt4.QtCore import  Qt
from myui import Ui_Dialog

from datetime import datetime
import PyQt4, PyQt4.QtGui, sys
import excel_get
from opentel import Logon,os



HOST=None
tn =telnetlib.Telnet()

#from pc_qiubai import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
	""" 
	Class documentation goes here. 
	"""
	#global times_print
	#times_print=1
	def __init__(self, parent=None):
		""" 
		Constructor 
		"""
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.user="root"
		self.password = "dvrs16"
		self.now_days = []
		self.times_write = 0
		self.path_pinjie = os.getcwd() + '\\dll\\'

		#self.pushButton.released.connect(self.on_pushButton_released)

	def time_format(self):#获取当天时间，写入最新检查时间时使用
		now=datetime.now()
		now_for=now.strftime('%Y/%m/%d')
		return now_for

	def get_ip(self):
		self.ip1=self.lineEdit.text()
		self.ip2=self.lineEdit_2.text()
		self.ip_list =[self.ip1,self.ip2]
		self.order1=self.lineEdit_5.text()
		self.order2=self.lineEdit_6.text()
		self.order_list=[self.order1,self.order2]
		pass

	@pyqtSignature("")
	def on_pushButton_released(self):
		""" 
		Slot documentation goes here. 
		"""
		self.times_print = 1
		self.get_ip()
		# TODO: not implemented yet
		# raise NotImplementedError
		#for ip in self.ip_list:
		self.HOST=self.ip_list
			#print type(ip)
			#print isinstance(ip,int)

		threads=[]
		from TelThread import DoThread
		#for ip in
		nips=range(len(self.ip_list))
		norders=range(len(self.order_list))
		order_list_old = self.order_list
		orders_new=[]
		for m in norders:
			#print order_list_old[m]
			#判断是否是QT的字符串类型，是则转为标准字符串加到新list。
			if isinstance(order_list_old[m],PyQt4.QtCore.QString):
				orders_new.append(str(order_list_old[m]))
			else:
				orders_new.append(order_list_old[m])
		print orders_new
		#print order_list
		#for order in nips:
		for ip in nips:        #以ip为循环条件，每个ip执行多条命令。
			#self.dodo=DoThread((str(HOST[ip]),user,password,self.order_list[0],self.order_list[1]))
			self.dodo = DoThread((str(self.HOST[ip]), self.user, self.password,self.path_pinjie, orders_new))
			#self.textBrowser_Back_1.append(self.HOST[ip])
			threads.append(self.dodo)
		for i in nips:
			#threads[i].lock()
			try:
				threads[i].stop()
			except Exception as th:
				print Exception,':',th
			threads[i].finishSignal.connect(self.Dodoend,Qt.QueuedConnection)
			#if threads[i]::isRunning()const:
				#print threads[i].is_alive()
			threads[i].start()
			threads[i].wait()
			#threads[i].stop()
			#threads[i].wait()
	#threads[i].unlock()
		#for i in nips:
			#threads[i].join()
		####################
		

	def Dodoend(self,gg):
		self.pushButton.setDisabled(True)
		#print gg
		#self.textBrowser_Back.clear()
		if self.times_print==1:
			self.textBrowser_Back_1.append(gg[1])
			self.textBrowser_Back_1.append(gg[0][0])
			#print gg
			print '1111111111111111111111111111111'
		elif self.times_print==2:
			self.textBrowser_Back_2.append(gg[1])
			self.textBrowser_Back_2.append(gg[0][0])
			#print gg
			print '1111111111111111111111111111111'
		print 'over'
		self.pushButton.setDisabled(False)
		self.times_print += 1

	@pyqtSignature("")
	def on_pushButton_2_clicked(self):
		self.textBrowser_Back_1.clear()
		self.textBrowser_Back_2.clear()

	def get_excel_all(self):
		self.excel_sour = self.lineEdit_3.text()
		self.excel_dst = self.lineEdit_4.text()
		# 从excel_get中取返回值
		self.get_ip_do = excel_get.GetIp()
		self.get_ip_excel_all = self.get_ip_do.update_content(str(self.excel_sour))

		#print self.get_ip_excel_all[1]
		return self.get_ip_excel_all

	@pyqtSignature("")
	def on_pushButton_3_released(self):
		self.get_excel_all()
		self.get_ip_excel = self.get_ip_excel_all[0]
		print self.get_ip_excel
		self.get_ip()
		#print str(self.excel_sour)
		self.ip_last=[]
		self.text_all=[]
		self.temp_longdays=self.get_ip_excel_all[1]
		self.temp_nowdays =self.get_ip_excel_all[2]
		#print 'temp is: ',temp_longdays
		#ll=[]
		self.list_long_days=[int(num) for num in self.temp_longdays if isinstance(num,float)]
		self.list_get_now_days=[int(num) for num in self.temp_nowdays if isinstance(num,float)]
		#print list_long_days

		#print 'self.get_ip_excel'

		# TODO: not implemented yet
		# raise NotImplementedError
		# for ip in self.ip_list:
		self.HOST_excel = self.get_ip_excel
		# print type(ip)
		# print isinstance(ip,int)
		#user = "root"
		#password = "dvrs16"
		threads = []
		from TelThread import DoThread
		# for ip in
		nips_excel = range(len(self.HOST_excel))
		norders_excel = range(len(self.order_list))
		order_list_old_excel = self.order_list
		orders_new_excel = []
		for m in norders_excel:
			# print order_list_old[m]
			# 判断是否是QT的字符串类型，是则转为标准字符串加到新list。
			if isinstance(order_list_old_excel[m], PyQt4.QtCore.QString):
				orders_new_excel.append(str(order_list_old_excel[m]))
			else:
				orders_new_excel.append(order_list_old_excel[m])
		#print orders_new
		# print order_list
		# for order in nips:
		for ip in nips_excel:  # 以ip为循环条件，每个ip执行多条命令。
			# self.dodo=DoThread((str(HOST[ip]),user,password,self.order_list[0],self.order_list[1]))
			self.dodo_excel = DoThread((str(self.HOST_excel[ip]), self.user, self.password, self.path_pinjie,orders_new_excel))
			# self.textBrowser_Back_1.append(self.HOST[ip])
			threads.append(self.dodo_excel)
		#m=[]
		#n=''
		for i in nips_excel:
			# threads[i].lock()
			threads[i].finishSignal.connect(self.Doexcel, Qt.QueuedConnection)
			threads[i].start()
			threads[i].stop()
			threads[i].wait()
			#print 'mmmmmmmm',n
		#now_days=[]
		#now_days=m[-1]
		#print now_days
		#return self.get_ip_excel_all[1]

	def Doexcel(self,mm):
		self.pushButton_3.setDisabled(True)
		#print gg
		#self.textBrowser_Back.clear()
		print mm[0][0]
		get_contents=mm[0][0]
		self.text_all.append(get_contents)
		#输出第一个值：产品当前运行时长，单位是天。
		sel_days_now=pre_re=re.findall(r'(\d{0,3})\sday',get_contents)
		if sel_days_now:
			sel_days_now=int(''.join(sel_days_now))
		else:
			sel_days_now=0

		self.now_days.append(sel_days_now)
		print self.now_days

		#输出第二个值：检查日期
		time_for_excel=self.time_format()

		#输出第三个值：最长时间
		print self.get_ip_excel_all[1]
		'''
		temp_longdays=self.get_ip_excel_all[1]
		temp_nowdays =self.get_ip_excel_all[2]
		#print 'temp is: ',temp_longdays
		#ll=[]
		list_long_days=[int(num) for num in temp_longdays if isinstance(num,float)]
		list_get_now_days=[int(num) for num in temp_nowdays if isinstance(num,float)]
		print list_long_days
		'''
		#判断，如果当前天数小于最大天数，则不变；如果当前天数大于最大天数，则置最大天数为当前天数
		if sel_days_now<= self.list_long_days[self.times_write]:
			pass
		else:
			self.list_long_days[self.times_write]=sel_days_now
			print "Change long day to now day!!!",self.list_long_days[self.times_write]
		print mm[1][11:]
		self.ip_last.append(mm[1][11:])
		print u'现在是第：%s个' %self.times_write
		print u'当前天数是：',sel_days_now,'\n'
		print u'最大天数是：',self.list_long_days[self.times_write],'\n'
		status_now=[]
		if sel_days_now>=self.list_get_now_days[self.times_write]:
			status_now.append(u'正常')
		else:
			status_now.append(u'异常')

		self.times_write += 1

		if len(self.now_days)==len(self.HOST_excel):
			print '=========================='
			self.write_excel_all = self.get_ip_do.write_excel(str(self.excel_sour),str(self.excel_dst),self.list_long_days,self.now_days,time_for_excel,status_now,self.ip_last,self.text_all)
			print '--------------------------'

		self.pushButton_3.setDisabled(False)
		#sour_path, dst_path, long_day, now_day, now_date
		#self.excel_sour
		#self.excel_dst
		#self.pushButton.setDisabled(False)
		'''
		if self.times_print==1:
			self.textBrowser_Back_1.append(mm[1])
			self.textBrowser_Back_1.append(mm[0][0])
			#print gg
			print '1111111111111111111111111111111'
		elif self.times_print==2:
			self.textBrowser_Back_2.append(gg[1])
			self.textBrowser_Back_2.append(gg[0][0])
			#print gg
			print '1111111111111111111111111111111'
		print 'over'
		self.pushButton.setDisabled(False)
		self.times_print += 1
		'''
		#return sel_days_now

	@pyqtSignature("")
	def on_pushButton_4_released(self):
		self.get_ip()
		self.pushButton_4.setDisabled(True)
		status_telback=[]
		for ip_in in self.ip_list:
			msg_err = QMessageBox(QMessageBox.Warning, u"注意: "+str(ip_in), u"出问题了，检查一下吧！")
			try:
				Logon(str(ip_in),self.path_pinjie)
				#status_telback.append(str(ip_in))
				text_output = str(ip_in) + ' ok'
				self.label_7.setText(text_output)
			except Exception as err:
				print Exception,':',err
				msg_err.exec_()
		#text_output=status_telback[0]+'\n'+status_telback[1]+' ok'
		self.pushButton_4.setDisabled(False)


if __name__ == '__main__':
	app = PyQt4.QtGui.QApplication(sys.argv)
	msg_box = QMessageBox(QMessageBox.Warning,u"恭喜：",u"转换完毕！")
	msg_flase= QMessageBox(QMessageBox.Warning,u"注意：",u"出问题了，检查一下吧！")
	dlg = Dialog()
	dlg.show()

	sys.exit(app.exec_())

# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox
import threading
import time
import re
import telnetlib
from opentel import Logon,os
tn =telnetlib.Telnet()



# 继承 QThread 类
class DoThread(QtCore.QThread):
	"""docstring for BigWorkThread"""
	# 声明一个信号，同时返回一个list，同理什么都能返回啦
	finishSignal = QtCore.pyqtSignal(list)

	# 构造函数里增加形参
	def __init__(self, args, parent=None):
		#threading.Thread.__init__(self)
		super(DoThread, self).__init__(parent)
		#QtCore.QThread.__init__(self, parent)
		# 储存参数
		self.args = args
		self.mutex = QtCore.QMutex()
		self.stopped = False
		self.completed = False

	def stop(self):
		try:
			self.mutex.unlock()
			self.stopped =True
		finally:
			self.mutex.unlock()

		#self.wait()
	# 重写 run() 函数，在里面干大事。
	def run(self):
		# 大事
		# msg_box = QMessageBox(QMessageBox.Warning, u"恭喜：", u"转换完毕！")
		# msg_flase = QMessageBox(QMessageBox.Warning, u"注意：", u"出问题了，检查一下输入值吧！")
		#try:
			# excel_zhuanhuan=jing(self.args[0],self.args[1],self.args[2],self.args[3])
			# self.chushigu, self.chushimoney, self.yuetou,self.bili)
			# print '初始G: ',excel_zhuanhuan[0]
			# print '初始M: ',excel_zhuanhuan[1]
			#s = int(self.args[2])
		output_list = []
		HOST=self.args[0]
		user=self.args[1]
		password = self.args[2]
		self.path_dll=self.args[3]
		self.order_list=self.args[4]
		try:
			#Logon(HOST,self.path_dll)
			time.sleep(5)
			tn.open(HOST)
			if tn.open:
				# tn.read_until(b"login: ")
				if tn.read_until(b"login: "):
					tn.write(user.encode('ascii') + b"\n")
				else:
					print 'no user'
				tn.read_until(b"Password: ")
				tn.write(password.encode('ascii') + b"\n")
				print 'ok'
				tn.write(b'\n')
				time.sleep(1)
				for order_one in self.order_list:
					tn.write(str(order_one).encode('ascii') + b'\n')
					time.sleep(2)
				tn.write(b"exit\n")
				#self.mutex.lock()
				temp_print = tn.read_very_eager()
				temp_print.strip().decode('utf-8')
				time.sleep(1)
				result, number = re.subn(r'\[\d.*?m', '', temp_print)

				if result:
					output_list.append(result)
					print '###########################'
				else:
					print 'No result at here!!!Check TelThread_run!'
				self.completed = True
			#return output_list
				print type(HOST)
				self.finishSignal.emit([output_list,HOST])
				#self.mutex.unlock()
		# time.sleep (2)

		except Exception, e:
			#msg_flase.exec_()
			print Exception, ":", e
			print u'Oh no !!! 拷贝黑色控制台中所有内容保存发送作者吧！'

		# 大事干完了，发送一个信号告诉主线程窗口


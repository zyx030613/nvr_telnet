# coding=utf-8
import ctypes
import time,os,sys
os.path.abspath('.')
from ctypes import *

iServerPort = 0
iClientPort = 6699
iWnd = 0

cProxy = ""
#ctypes.POINTER(c_char("/0")*2)
#cProxyn =cProxy()
#cIP = c_char_p(b'192.168.18.138')
cUserName = c_char_p(b'Admin')
cUserName1 = cUserName
cPassword = c_char_p(b'1111')
pcProductID = ""
iPort = c_int(3000)

#if __name__ == '__main__':
def Logon(ip,dll_path):
    #加载

    cIP=c_char_p(ip)
    #ppp=os.path.split(os.path.realpath(__file__))[0]
    #print ppp+'\\'+'NVSSDK.dll'
    os.chdir(dll_path)
    dll = ctypes.windll.LoadLibrary('NVSSDK.dll')
    dllTest = dll.NetClient_Startup_V4
    #print(dllTest)
    dllTest.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
        # _iServerPort,ctypes.c_int_iClientPort,ctypes.c_int_iWnd
        # dllTest.Serverport = ctypes.c_int_iServerPort
        # 发送SDK初始化
    nSet = dllTest(iServerPort, iClientPort, iWnd)
    #print'Logon ID is: ',nSet
    time.sleep(2)

    #登录
    dllLogOn = dll.NetClient_Logon
    #dllLogOn.argtypes = [c_char_p,c_char_p,c_char_p,c_char_p,c_char_p,c_int]
    #print (cProxy,cUserName,cPassword,iPort)
    #发送登录信息
    dllLogOnSet = dllLogOn (cProxy,cIP,cUserName,cPassword,pcProductID,iPort)
    time.sleep(3)

    dllLogOn.restype = ctypes.c_int
    print 'Logon id is: ',dllLogOnSet
    #print (dllLogOn.restype())

    dllGetLogonStatus = dll.NetClient_GetLogonStatus
    dllGetLogonStatus.argtypes = [c_int]
    dllGetSet = dllGetLogonStatus(dllLogOnSet)
    time.sleep(5)
    print 'Logon Status is: ',dllGetSet,u'(0和1都正常)'
    try:
        dllChangeTel = dll.NetClient_SetCommonEnable
        dllChangeTel.restype =ctypes.c_int
        dllTelSet=dllChangeTel(dllLogOnSet,0x12014,0x7FFFFFFF,1)
        print ip,u'开启成功！'
        #dllSettt=dllC
    except Exception as e:
        print (Exception,e)
        print u'报错啦，把错误信息发给zyx吧!!'
    time.sleep(3)


#Logon()
'''
    dllGetVersion = dll.NetClient_GetServerVersion_V1
    dllGetVersion.argtypes =[c_int]
    dllGetVersionSet = dllGetVersion(dllLogOnSet)
    print (dllGetVersion)

    #class testdll(Structure):
        #_fields_ = [('m_ulMajorVersion', c_int),
                    #('b', c_char_p)]

    if dllGetSet == 0:
        dllReboot = dll.NetClient_Reboot
        dllReboot.argtypes = [c_int]
        dll.RebootSet = dllReboot(dllLogOnSet)
        print ( 'reboot ok!')
    else:
        dllLogoff = dll.NetClient_Logoff
        dllLogoff.argtypes =[c_int]
        dll.LogoffSet = dllLogoff(dllLogOnSet)
        print ('Logon is not ok!')

'''



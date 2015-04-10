#!env python

from pygsm import GsmModem

gsm = GsmModem(port="COM22",baudrate=115200,logger=GsmModem.debug_logger).boot()

s = gsm.wait_for_network()
#gsm.send_sms('+256784726116', 'This is a message')
numbers=['+256779127009','+256782481746']
for number in numbers:
	gsm.send_sms(number, 'This is a message from a modem')
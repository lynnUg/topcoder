#!env python
import serial
import time
print "here"
#m = serial.Serial('COM16', 115200, timeout=1)
#m.write('ATZ\r')
#m.write('AT+CMGF=1\r\n')
#m.write('AT+CMGS="%s"\r\n' % '+256781057175')
#m.write('this is the text message here')
#m.write(chr(26))
#m.close()
import sms 
m = sms.Modem('COM16')
msgs=m.messages()
print msgs[0].number
print msgs[0].text
print m.sent()
#m.send('+256781057175', 'This is a message')
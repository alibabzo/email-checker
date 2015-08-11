import imaplib, time, serial, sys

try:
    ser = serial.Serial(4)
except serial.SerialException:
    print ("Serial thing went wrong")
    time.sleep(2)
    sys.exit()
    
obj = imaplib.IMAP4_SSL('imap.gmail.com','993')
obj.login('alistair.bill','CENSORED')
obj.select('INBOX')
newMails = len(obj.search(None,'UnSeen')[1][0].split())

if newMails > 0:
    ser.write(b'M')
else:
    ser.write(b'N')

ser.close()


        
	

	




        

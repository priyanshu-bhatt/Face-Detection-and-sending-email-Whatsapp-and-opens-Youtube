import cv2
cap=cv2.VideoCapture(0)
model=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


while True:
    ret,photo=cap.read()
    face=model.detectMultiScale(photo)
    if len(face)==0:
        pass
    else:
        x1=face[0][0]
        y1=face[0][1]
        x2=x1+face[0][2]
        y2=y1+face[0][3]
        
    aphoto=cv2.rectangle(photo,(x1,y1),(x2,y2),[0,255,0],2)
    cv2.imshow('title',photo)
    if cv2.waitKey(3)==13:
        break
        
        
        
cv2.destroyAllWindows()
if len(face)!=0:
    import smtplib
    server=smtplib.SMTP_SSL("smtp.gmail.com.",465)
    server.login("****YOUR EMAIL ID HERE*****","******YOUR ID PASSWORD HERE")
    server.sendmail("*****YOUR ID HERE","****THE RECIEVER ID HERE******","*****FACE DETECTED*****(YOUR MSG)")
    server.quit()
    import pywhatkit as py
    py.playonyt("Cruel World-Faya||Priyanshu Bhatt(VIDEO NAME)")
    py.sendwhatmsg("+91{PHONE NUMBER }","*****FACE DETECTED ****",TIME,MIN,TIME AFTER WHICH MSG WILL BE SEND)
    
     
    
else:
    pass 


cap.release()
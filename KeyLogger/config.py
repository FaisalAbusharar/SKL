import json
import os

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
class newConfig():

    

    def print_data():
        with open("./config.json","r") as pf:
            return json.load(pf)
        

    def edit_data():
        with open("./config.json", "r") as ef:

            parsed = json.load(ef)

            Mode = parsed["mode"]
           
     
            senderEmail = input(bcolors.FAIL + "Sender Email: "+ bcolors.WHITE)
            senderPassword = input(bcolors.FAIL + "Sender Password: "+ bcolors.WHITE)
            recieverEmail = input(bcolors.OKGREEN + "Receiver Email: " + bcolors.WHITE)

            with open("./config.json", "w") as ev:           
                new = {'sender_email': senderEmail, 'receiver_email': recieverEmail, 'sender_password': senderPassword, "mode": Mode}
                json.dump(new,ev)
            
            print(bcolors.WARNING + "Data changed.")
            return bcolors.WHITE    
        
    def mode():
          os.system("cls")
          printlogo()
          with open("./config.json", "r") as ef:

            parsed = json.load(ef)
           
     
            senderEmail = parsed["sender_email"]
            senderPassword = parsed["sender_password"]
            recieverEmail = parsed["receiver_email"]

            print(bcolors.FAIL + "Please select, (email) or (local) mode")
            Mode = input(bcolors.WHITE + "")

            if Mode in modes:
                print(bcolors.WARNING + "Data Changed.")

                with open("./config.json", "w") as ev:
                    new = {'sender_email': senderEmail, 'receiver_email': recieverEmail, 'sender_password': senderPassword, "mode": Mode}
                    json.dump(new,ev)

            else:
                input(bcolors.DIM + bcolors.FAIL + "Invaild Option, try again...")
                newConfig.mode()

            return bcolors.WHITE   

            
     



import os

host = input("Write ip: ")
default_host = "10.8.45.140"

if host == "":
    host = default_host

def ping(ip):
    response = os.system("ping -c 1 " + ip + " > /dev/null 2>&1")
    if response == 0:
        return True
    return False

beep = lambda x: os.system("play -n synth 0.05 sine 880 vol 1 > /dev/null 2>&1;" * x)

cont = 1
os.system("clear")
online = False
while True:
    if ping(host) == True:
        os.system("clear")
       
        text = "\n\n\t\t\t" + host + " IS ONLINE"
        if host == default_host:
            text += "\n\t\t    You have FREE INTERNET, Enjoy :)"
       
        print(text)

        if online == False:
            beep(3)
            online = True
    else:
        os.system("clear")
        print("OFFLINE: ", host)
        print("Attempts: ", cont)
        cont += 1
        online = False
import os

host = input("Write ip: ")
#default_host = "10.8.45.140"
default_host = "10.8.16.254"

if host == "":
    host = default_host

text = "\n\n\t\t\t" + host + " IS ONLINE\n\n"

# response = os.system("ping -c 1 " + default_host) -> para Windows

def ping(ip):
    response = os.system("ping -c 1 " + ip + " > /dev/null 2>&1")
    if response == 0:
        return True
    return False

def writeFile():
        file = open('alerta.txt', 'w')
        file.writelines(text)
        file.close()

beep = lambda x: os.system("play -n synth 0.05 sine 880 vol 1 > /dev/null 2>&1;" * x)

cont = 1
os.system("clear")
online = False
while True:
    if ping(host) == True:
        writeFile()

        os.system("clear")
        print(text)

        if online == False:
            beep(3)
            online = True
        #break
    else:
        os.system("clear")
        print("OFFLINE: ", host)
        print("Attempts: ", cont)
        cont += 1
        online = False
        #os.system("pkill gedit")
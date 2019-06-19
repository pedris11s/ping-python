import os

host = input("Write ip: ")
#hostname = "10.8.45.140"
hostname = "localhost"

if host == "":
    host = hostname

text = "\n\n\t\t\t" + host + " IS ONLINE\n\n"

# response = os.system("ping -c 1 " + hostname) -> este seria para Windows

def ping(ip):
    response = os.system("ping -c 1 " + ip + " > /dev/null 2>&1")
    if response == 0:
        return True
    return False

def writeFile():
        file = open('alerta.txt', 'w')
        file.writelines(text)
        file.close()

beep = lambda x: os.system("play -n synth 0.1 sine 880 vol 0.5 > /dev/null 2>&1;" * x)

cont = 1
os.system("clear")
while True:
    print("Trying to reach the host...")
    if ping(host) == True:
        writeFile()
        #os.system("play sonido.mp3")
        #os.system("play -n synth 0.1 sine 880 vol 0.5")
        beep(3)
        os.system("clear")
        print(text)
        #os.system("clear")
        #os.system("gedit alerta.txt")
        break
    else:
        os.system("clear")
        print("OFFLINE: ", host)
        print("Attempts: ", cont)
        cont += 1
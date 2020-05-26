import socket
def getInfor():
    global HOST_NAME
    HOST_NAME = socket.gethostname()
    global HOST_ADDRESS
    HOST_ADDRESS = socket.gethostbyname(HOST_NAME)
    print(HOST_ADDRESS)


def ChoosePort():
    global PORT
    PORT = int(input("Please choose a port that will be used for connection?"))


def CreateServer():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    soc.bind((HOST_ADDRESS, PORT))
    soc.listen(5)
    while True:
        Clientconnection, ClientAddr = soc.accept()
        print("Connect to Client ", ClientAddr)
        while True:
            content = input("Enter your rieciver client ")
            Clientconnection.send(content.encode())
            content3 = Clientconnection.recv(1024).decode()
            print(content3)
        #while True:

            # content2=Clientconnection.recv(1024).decode()
        #print(content2)
        """
        content3=Clientconnection.recv(1025).decode()
        print(content3)
        content4=input("Enter your Information!!!")
        Clientconnection.send(content4.encode())"""


if __name__ == '__main__':
    getInfor()
    ChoosePort()
    CreateServer()

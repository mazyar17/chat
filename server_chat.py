import socket

s = socket.socket()

x = input('port :')

ip='192.168.43.96'

port = x



s.bind((ip , port))
s.listen()
print("Wait for client...")
c, addr=s.accept()
print("hey mazyar!! client added!!!!")
while True:
    msg=input("Your message-->>")
    c.send(msg.encode())
    print("client massege>>> : ",c.recv(1000).decode())

#server
#ip host=localhost

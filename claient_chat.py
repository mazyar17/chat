import socket

s=socket.socket()

mazyar = input('port :')

ip='192.168.43.96'
port = mazyar

s.connect((ip,port))
print("hey connect server mazyar! welcome!")
while True:
    print("server mazyar massege>>> : ",s.recv(1000).decode())
    msg = input("your massege-->>")
    s.send(msg.encode())

#claient

import socket
import sys

HOST=''
PORT=5789

soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    soc.bind((HOST, PORT))

except socket.error as message:
    print('Bind failed:'+str(message[0])+'message'+str(message[1]))
    sys.exit()

print.listen(9)

conn, address=soc.accept()
print('connected with'+ address+ ':'+str(address[1]))


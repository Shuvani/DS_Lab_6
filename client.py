import socket, sys, os

# read file name server address and port from command line
file_name = sys.argv[1]
server_addr = sys.argv[2] # 'localhost'
server_port = sys.argv[3] # 8800

# create socket
sock = socket.socket()

# connect to the server
sock.connect((server_addr, int(server_port)))

# send to the server file name
sock.sendto(file_name.encode(),(server_addr, int(server_port)))

# get file size
size = os.path.getsize(file_name)
if size == 0:
    percent = 99
else:
    percent = 0
# compute how many bites we should send to get 1% from 100%
progress_1 = round(size/100)
# open file
file = open(file_name, 'rb')
# while there is a content - send it
while True:
    # read portion of data from file
    content = file.read(progress_1)
    if not content:
        break
    sock.sendto(content, (server_addr, int(server_port)))
    percent += 1
    if percent <= 100:
        output = str(percent) + ' %...'
        print(output, end=' ')
file.close()

# закроем соединение
sock.close()

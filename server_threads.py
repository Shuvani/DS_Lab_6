import socket, threading, os

# we can have several clients at the same moment
clients = []

class ClientThread(threading.Thread):

    def __init__(self, conn, addr, name):
        # for each client we create mew thread and give name to it and append in the clients array
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.name = name
        clients.append(self.conn)
        print(str(self.addr) + ' connected as ' + self.name)
        self.run()

    def save_file(self, data):
        num = 1
        # we need to transform data into string
        data = str(data)
        # first of all we need to divide file name into name and extension
        i = 0
        while data[i] != '.':
            i += 1
        name = data[2:i]
        extension = data[i:(len(data)-1)]
        # now we know file name
        file_name = name + extension
        while os.path.exists(file_name):
            file_name = name + '_copy' + str(num) + extension
            num += 1
        file = open(file_name, "wb")
        return file

    # get file and save it
    def run(self):
        counter = 1
        while True:
            # we receive data
            data = self.conn.recv(1024)
            # if there is no more data - we stop the process and close everything
            if not data:
                break
            # if this is te first portion of data - this is file name
            if counter == 1:
                file = self.save_file(data)
            # if this is not the first portion of data - we write this data in the file
            else:
                file.write(data)
            counter += 1
        print("Data was received")
        file.close()
        self.close()

    # close connection
    def close(self):
        clients.remove(self.conn)
        self.conn.close()
        print(self.name + ' disconnected')

# create socket
sock = socket.socket()

# определимся с хостом и портом - строка хоста пустая чтобы сервер был доступен все интерфейсам
sock.bind(('', 8800))

# server can work only with four clients in a time - because I want such constraint. It can be easily changed
while len(clients) < 4:
    # star listening
    sock.listen()
    print("\nListening for incoming connections...")
    # accept client - get client address and add name
    conn, addr = sock.accept()
    name = 'user' + str(len(clients)+1)
    # create new thread for the client
    newclient = ClientThread(conn, addr, name)

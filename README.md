# DS_Lab_6
This is the DS course project which consists of two parts - server script which create new threads for the new clients to get files from them, and client which can send the file to the server.

### I. Local machine
1. User can run server on his local machine by command "python server_threads.py"
2. For client use command "python client.py [name_of_the_file_to_transfer] localhost 8800" 
3. If file with such name did not exist on the server side server will save it with the same name, if such file name has existed already server will add _copy[num] to the name of the file and will save it.

### AWS
1. For client use command "python client.py [name_of_the_file_to_transfer] 35.181.90.30 8800" 
2. If file with such name did not exist on the server side server will save it with the same name, if such file name has existed already server will add _copy[num] to the name of the file and will save it.

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    with s:
        while True:
            cmd = input('>')
            if cmd != '':
                cmd = str.encode(cmd)
                s.sendall(cmd)
                data = s.recv(1024)

                if data == b"quit":
                    break
                else:
                    print('######Received######\n', data.decode('utf-8'))

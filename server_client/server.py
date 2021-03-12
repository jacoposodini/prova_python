import socket
import subprocess

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

commands = {b'list':b'ls', b'concat':b'cat', b'print':b'echo'}
help_str = b"A simple server that map the following commands to the equivalent linux version:\n\
            list --> ls\n\
            concat --> cat\n\
            print --> echo\
            \n\n\"quit\" terminate the connection"

#list_files = subprocess.run(["ls"], stdout=subprocess.PIPE)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #per evitare il lock della porta
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    
    print('Connected by', addr)
    
    with conn:
        while True:        
            
            data = conn.recv(1024)
            
            if data != b'':
            
                cmd_split = data.split()
                cmd = cmd_split[0]
            
                #conn.sendall(data) #echo
                
                if cmd == b'help':
                    conn.sendall(help_str)
            
                elif cmd in commands:
                    command = [commands[cmd]]+cmd_split[1:]
                    cmd_return_string = subprocess.run(command, stdout=subprocess.PIPE)      
                    conn.sendall(cmd_return_string.stdout)
                elif data == b"quit":
                    conn.sendall(data)                
                    break
                else:
                    conn.sendall(b"Can't recognize the command! Try help")
                    
            

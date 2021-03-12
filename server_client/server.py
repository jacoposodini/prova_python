import socket
import subprocess

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

#commands is a dict in this form: {SERVER_COMMAND:[LINUX_COMMAND,MIN_PARAM]}

commands = {b'list':[b'ls',0], b'concat':[b'cat',1], b'print':[b'echo',0]}
help_str = b"A simple server that map the following commands to the equivalent linux version:\n\
            list --> ls\n\
            concat --> cat\n\
            print --> echo\
            \n\n\"quit\" terminate the connection"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #to avoid lock of the port
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
                    if commands[cmd][1] <= len(cmd_split) - 1: #are there enought parameters?
                        command = [commands[cmd][0]] + cmd_split[1:]
                        cmd_return = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        
                        if cmd_return.returncode != 0:
                            conn.sendall(b"Non zero return code while executing server command. MSG:\n" + cmd_return.stderr)
                        else:                   
                            conn.sendall(cmd_return.stdout)
                    else:
                        conn.sendall(b"Not enought parameters")
                elif data == b"quit":
                    conn.sendall(data)                
                    break
                else:
                    conn.sendall(b"Can't recognize the command! Try help")
                    
            

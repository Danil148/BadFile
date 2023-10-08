import socket


SERVER_HOST = '192.168.0.0' # IPv4 пк к которому будем подклюяаться
SERVER_PORT = 12345 # Порт по которому запущен сервер (BadFile)

while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        client_socket.connect((SERVER_HOST, SERVER_PORT))

        message = input("Комманда:   ")
        client_socket.send(message.encode('utf-8'))
        
        print(client_socket.recv(1024).decode('utf-8'))
        
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")

    finally:
        client_socket.close()

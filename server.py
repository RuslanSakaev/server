import html
import socket
import threading
from collections import deque

message_queue = deque(maxlen=10)
message_lock = threading.Lock()

def handle_client(client_socket, client_id):
    try:
        client_socket.send("Enter your name: ".encode('utf-8'))
        client_name = client_socket.recv(1024).decode('utf-8')
        welcome_message = f"Welcome, {client_name}! You are connected.\n"
        client_socket.send(welcome_message.encode('utf-8'))

        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                print(f"Client {client_id} disconnected")
                break
            data = data.strip()
            if data:
                data = html.escape(data)
            
            # Запись в историю
            with open("chat_history.txt", "a") as history_file:
                history_file.write(f"{client_name}: {data}\n")
            
            response = f"{client_name}, you sent: {data}"
            client_socket.send(response.encode('utf-8'))
            
    except ConnectionResetError:
        print(f"Client {client_id} forcibly disconnected")
    finally:
        client_socket.close()

def main():
    server_ip = '0.0.0.0'
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)
    print(f"Server listening on {server_ip}:{server_port}")

    client_id_counter = 0

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
        
        client_id = client_id_counter
        client_id_counter += 1
        
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_id))
        client_handler.start()

if __name__ == "__main__":
    main()
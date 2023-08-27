import socket
import threading
import time
import fcntl
import os

def receive_messages():
    while True:
        try:
            with open("chat_history.txt", "r") as history_file:
                # Получаем файловую блокировку
                fcntl.flock(history_file, fcntl.LOCK_SH)
                lines = history_file.readlines()
                fcntl.flock(history_file, fcntl.LOCK_UN)  # Освобождаем блокировку
                for line in lines:
                    print(line.strip())
        except FileNotFoundError:
            pass
        except Exception as e:
            print("Error while reading chat history:", e)
        time.sleep(2)  # Ожидаем некоторое время перед следующим чтением

def main():
    server_ip = '127.0.0.1'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    client_name = input("Enter your name: ")
    client_socket.send(client_name.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(response)

    message_receiver = threading.Thread(target=receive_messages)
    message_receiver.start()

    try:
        while True:
            message = input()
            client_socket.send(message.encode('utf-8'))
    except KeyboardInterrupt:
        pass
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()


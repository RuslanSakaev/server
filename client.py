import socket
import threading
import time

def receive_messages(client_socket):
    last_message_count = 0

    while True:
        try:
            with open("chat_history.txt", "r") as history_file:
                lines = history_file.readlines()
                new_messages = lines[last_message_count:]

                for line in new_messages:
                    print(line.strip())
                    last_message_count += 1
        except FileNotFoundError:
            pass
        except Exception as e:
            print("Error while reading chat history:", e)
        time.sleep(2)   # Ожидаем некоторое время перед следующим чтением

def main():
    server_ip = '127.0.0.1'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    client_name = input("Enter your name: ")
    client_socket.send(client_name.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(response)

    message_receiver = threading.Thread(target=receive_messages, args=(client_socket,))
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

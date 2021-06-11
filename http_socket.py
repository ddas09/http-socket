import socket as sock
import sys


def sendHttpRequest(choice, socket):
    if choice == '1':
        req = "GET / HTTP/1.1\r\nHost:localhost\r\nConnection: close\r\n\r\n"
    elif choice == '2':
        req = "GET /api/stocks/ HTTP/1.1\r\nHost:localhost\r\nConnection: close\r\n\r\n"
    elif choice == '3':
        id = input("Enter stock id: ")
        req = f"GET /api/stocks/{id}/ HTTP/1.1\r\nHost:localhost\r\nConnection: close\r\n\r\n"
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    else:
        return "Invalid choice"

    # Send request to server
    socket.sendall(req.encode())
    response = ''
    while True:
        server_response = client_socket.recv(4096)
        if not server_response:
            break
        else:
            response += server_response.decode()

    return response


if __name__ == '__main__':
    server_ip = '127.0.0.1'
    server_port = 8000
    
    while True:
        print("\n1. Index Page\n2. Get all stocks\n3. Get stock by id", end="")
        print("\n4. Insert new stock\n5. Update a stock\n6. Delete a stock\n7. Quit\n")
        choice = input("Enter your choice: ")
        if choice == '7':
            sys.exit()

        # Create a socket for sending http request
        client_socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        response = sendHttpRequest(choice, client_socket)
        print(f"\nRESPONSE:\n{response}")
        client_socket.close()
  

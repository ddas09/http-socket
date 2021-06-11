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
        symbol = input("Enter stock symbol: ")
        name = input("Enter stock name: ")
        req_body = f'{{"symbol": "{symbol}", "name": "{name}"}}'
        data_length = len(req_body)
        req = "POST /api/stocks/ HTTP/1.1\r\nHost:localhost\r\nContent-Type: application/json"
        req += f"\r\nContent-Length:{data_length}\r\nConnection: close\r\n\r\n{req_body}"

    elif choice == '5':
        id = input("Enter the stock id to update: ")
        symbol = input("Enter new symbol: ")
        name = input("Enter new name: ")
        req_body = f'{{"symbol": "{symbol}", "name": "{name}"}}'
        data_length = len(req_body)
        req = f"PUT /api/stocks/{id}/ HTTP/1.1\r\nHost:localhost\r\nContent-Type: application/json"
        req += f"\r\nContent-Length:{data_length}\r\nConnection: close\r\n\r\n{req_body}"

    elif choice == '6':
        id = input("Enter the stock id to delete: ")
        req = f"DELETE /api/stocks/{id}/ HTTP/1.1\r\nHost:localhost\r\nConnection: close\r\n\r\n"
        
    else:
        return "Invalid choice"

    # Send request to server
    socket.sendall(req.encode())
    response = ''

    # Recieve all data packets
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
        print("\n1. Index page\n2. Get all stocks\n3. Get stock by id")
        print("4. Insert new stock\n5. Update a stock\n6. Delete a stock\n7. Quit\n")
        choice = input("Enter your choice: ")
        if choice == '7':
            sys.exit()

        # Create a socket for sending http request
        client_socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        response = sendHttpRequest(choice, client_socket)
        print(f"\nRESPONSE:\n{response}")
        client_socket.close()
  

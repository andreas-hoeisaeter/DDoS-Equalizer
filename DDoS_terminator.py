import time
import socket

print("1")

time.sleep(1)

print("2")

time.sleep(2)

print("3")

time.sleep(2)

print("\nAnimals shit, normal thing.\n")

print(10111)

print("\nStinks.\n")

breakdoes = input("Who do you want a crush? ")

print(breakdoes, "their broken!")

time.sleep(1)

print("Really broken?")

port = 80

try:

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((breakdoes, port))

    print(f"Successfully connected to {breakdoes} on port {port}!")

    response = client_socket.recv(4096)

    print(response.decode('utf-8', errors='ignore')[:500])

finally:

    client_socket.close()

time.sleep(2)

print("Really!")

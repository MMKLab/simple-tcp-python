from socket import *

# Staticke varijable
server_address = 'localhost'
server_port = 8090

# Pravljenje soketa - AF_INET za IPv4 protokol, SOCK_STREAM za TCP protokol
srv_socket = socket(AF_INET, SOCK_STREAM)

# Vezujemo napravljeni socket za svoju adresu, kao i za port na kom ce da slusa
srv_socket.bind((server_address, server_port))

# Slusa za konekcije
srv_socket.listen()
print('Waiting for connections . . .')

while True:
    # Prihvata konekciju klijenta
    client_socket, client_address = srv_socket.accept()

    # Prihvata recenicu koju je klijent poslao
    sentence = client_socket.recv(4096).decode()
    print('I received a new request! Processing this sentence:', sentence)

    # Obradjuje recenicu [start : end : step], idemo unazad, stoga je step -1
    sentence = sentence[::-1]

    # Salje recenicu nazad
    client_socket.send(sentence.encode())

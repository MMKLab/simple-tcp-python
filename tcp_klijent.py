from socket import *

# Staticke varijable
server_address = 'localhost'
server_port = 8090

# Cekamo unos sa tastature
sentence = input('Unesi neku recenicu')

# Pravljenje soketa - AF_INET za IPv4 protokol, SOCK_STREAM za TCP protokol
cl_socket = socket(AF_INET, SOCK_STREAM)

# Konektujemo se na server (gadjamo adresu servera i port na kom on slusa)
cl_socket.connect((server_address, server_port))

# Saljemo recenicu serveru
cl_socket.send(sentence.encode())

# Prihvatamo recenicu (i odmah je prikazujemo u konzoli)
print(cl_socket.recv(4096).decode())

import socket 
#t_host = 'www.google.com'
#t_port = 80
t_host = '104.236.251.76'
t_port = 81


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((t_host, t_port))
client.send("GET / HTTP/1.1\r\nHost google.com\r\n\r\n")
response = client.recv(4096)
print response
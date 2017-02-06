import time
import socket

host = '127.0.0.1'
port = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.settimeout(0.1)
sock.listen()

count = 0
while True:
    try:
        conn, addr = sock.accept()
        data = conn.recv(256)
        print('received: ', data)
        conn.sendall(b'OK')
        conn.close()
    except socket.timeout:
        pass

    print(count)
    count += 1
    with open('dummy.txt', 'w') as f:
        f.write('count: {}'.format(count))

    time.sleep(1.0)

import threading
import socket


def tcp_msg_proc(sock, addr, buffer_size):
    data = sock.recv(buffer_size)
    print(data)
    sock.send((data.decode('utf-8')).encode('utf-8'))
    sock.close()


def start(host, port, listen_num, buffer_size):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(listen_num)
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcp_msg_proc, args=(sock, addr, buffer_size))
        t.start()
        pass
    pass


import socket
import sys
import threading
from communication_config import HOST, PORT_A, PORT_B, FILE_SIZE_LIMIT


files = []
signatures = []
file_extensions = []


def save_file(chosen_file, file_path):
    with open(file_path, "wb") as f:
        f.write(chosen_file)


def receive_file(conn):
    with conn:
        while True:
            data = conn.recv(FILE_SIZE_LIMIT)
            if not data:
                break
            data_decoded = data.decode()
            if data_decoded[0] == 't':
                filename = '.txt'
            else:
                filename = ''
            limit_str = len(str(FILE_SIZE_LIMIT))
            iterator_start = 1
            iterator_end = limit_str
            file_size = int(data_decoded[iterator_start:iterator_end].strip())
            iterator_start = iterator_end + 1
            iterator_end = iterator_start + file_size
            file = data_decoded[iterator_start:iterator_end]
            print("File received")
            iterator_start = iterator_end
            iterator_end = iterator_start + limit_str
            xml_size = int(data_decoded[iterator_start:iterator_end].strip())
            iterator_start = iterator_end
            iterator_end = iterator_start + xml_size
            xml = data_decoded[iterator_start:iterator_end]
            files.append(file)
            signatures.append(xml)
            file_extensions.append(filename)
            print("Signature received")


def prepare_file_size(size):
    limit_str = len(str(FILE_SIZE_LIMIT))
    size_str = str(size)
    for _ in range(limit_str - len(size_str)):
        size_str += ' '
    return size_str


def send_file(host, port, file_path, file_type, xml_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open(file_path, 'rb') as f:
            with open(xml_path, 'rb') as xml:
                data = f.read()
                xml_data = xml.read()
                if len(data) > FILE_SIZE_LIMIT or len(xml_data) > FILE_SIZE_LIMIT:
                    raise Exception('File too large')
                file_size = prepare_file_size(len(data))
                xml_size = prepare_file_size(len(xml_data))
                if file_type == 'txt':
                    s.sendall(b't' + file_size.encode() + data + xml_size.encode() + xml_data)
                else:
                    s.sendall(b'b' + file_size.encode() + data + xml_size.encode() + xml_data)
                print("Package sent")


def main():
    if sys.argv[1] == 'A':
        port = PORT_A
        dest_port = PORT_B
    else:
        port = PORT_B
        dest_port = PORT_A

    def listen_for_files():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, port))
            s.listen()
            print("Listening on port: ", port)
            while True:
                conn, addr = s.accept()
                print('Connected with: ', addr)
                receive_thread = threading.Thread(target=receive_file, args=(conn,))
                receive_thread.start()

    listen_thread = threading.Thread(target=listen_for_files)
    listen_thread.start()

    while True:
        print('1. Send text file\n2. Send binary file\n3. Exit')
        choice = input("Choose option: ")
        if choice == '1':
            file_path = input('Input file path: ')
            xml_path = input('Input xml key path: ')
            send_file(HOST, dest_port, file_path, 'txt', xml_path)
        elif choice == '2':
            file_path = input('Input file path: ')
            xml_path = input('Input xml key path: ')
            send_file(HOST, dest_port, file_path, '', xml_path)
        elif choice == '3':
            break
        else:
            print('Invalid option')


if __name__ == "__main__":
    main()

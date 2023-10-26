import cv2
import frame as boxes
import socket
import threading
import runner
import time
import blessed

t = blessed.Terminal()
box = boxes.HDFrame((0, 0), (60, 30))

print('1. Host\n2. Client')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    if input('>>> ') == '1':
        cap = cv2.VideoCapture(1)
        s.bind(('', 7008))
        s.listen()
        sock, addr = s.accept()
        with sock:
            get = threading.Thread(
                target=runner.get,
                daemon=False,
                args=(sock, box)
            )
            send = threading.Thread(
                target=runner.send,
                daemon=False,
                args=(sock, cap)
            )
            send.start()
            get.start()
            get.join()
    else:
        cap = cv2.VideoCapture(1)
        s.connect((input('Host IP: '), 7008))
        time.sleep(1)
        get = threading.Thread(
            target=runner.get,
            daemon=False,
            args=(s, box)
        )
        send = threading.Thread(
            target=runner.send,
            daemon=False,
            args=(s, cap)
        )
        get.start()
        send.start()
        send.join()

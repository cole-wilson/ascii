# import socket
# import frame as boxes
# import numpy as np
# import pickle
# import blessed
# import struct
# import cv2
#
# term = blessed.Terminal()
#
# box = boxes.HDFrame((0, 0), (80, 40))
# a = boxes.ASCIIFrame((80, 0), (50, 40))
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# 	s.connect(('127.0.0.1', 7008))
# 	payload_size = struct.calcsize("L")
# 	data = b""
# 	while True:
# 		while len(data) < payload_size:
# 			data += s.recv(4096)
# 		packed_msg_size = data[:payload_size]
# 		data = data[payload_size:]
# 		msg_size = struct.unpack("L", packed_msg_size)[0]
# 		while len(data) < msg_size:
# 			data += s.recv(4096)
# 		frame_data = data[:msg_size]
# 		data = data[msg_size:]
# 		frame = pickle.loads(frame_data)
# 		box.draw(frame)
# 		a.draw(frame)

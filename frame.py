import sys
import blessed
import cv2
import numpy as np

term = blessed.Terminal()


class Frame:
	x = y = w = h = 0
	h_res = w_res = 1

	def __init__(self, pos, dimensions):
		self.x, self.y = pos
		self.w, self.h = dimensions
		self.h *= self.h_res
		self.w *= self.w_res

	def reposition(self, xy):
		self.x, self.y = xy

	def resize(self, dimensions):
		self.w, self.h = dimensions
		self.h *= self.h_res
		self.w *= self.w_res


	def draw(self, data):
		pass

	def fit(self, data):
		background = np.zeros((self.h, self.w, 3), np.uint8)
		h, w, channels = data.shape
		if h > w:
			height = self.h
			change = height / h
			width = round(change * w)
		else:
			width = self.w
			change = width / w
			height = round(change * h)
		data = cv2.resize(data, (width, height), fx=0.5, fy=0.5)
		y_offset = round((self.h - height)/2)
		x_offset = round((self.w - width)/2)
		background[y_offset:y_offset+height, x_offset:x_offset+width] = data
		return background


class HDFrame(Frame):
	h_res, w_res = 2, 1

	def draw(self, data):
		if data is None:
			return
		data = self.fit(data)
		row_num = 0
		row_y = 0
		for row in data[::2]:
			outrow = ""
			for x, pixel in enumerate(row):
				try:
					next_row_pixel = data[row_num + 1, x]
				except IndexError:
					next_row_pixel = (0, 0, 0)
				b = term.on_color_rgb(*reversed(pixel)) + term.color_rgb(*reversed(next_row_pixel)) + '▄'
				outrow += b
			sys.stdout.write(term.move_xy(self.x, self.y + row_y) + outrow)
			sys.stdout.flush()
			row_num += 2
			row_y += 1


class ASCIIFrame(Frame):
	def draw(self, data):
		if data is None:
			return
		data = self.fit(data)
		for y, row in enumerate(data):
			outrow = ""
			for x, pixel in enumerate(row):
				brightness = round(10 * (np.average(pixel)/255)) - 1
				outrow += term.on_color_rgb(0, 0, 0) + term.white +" .:-=+*#%@"[brightness]
			sys.stdout.write(term.move_xy(self.x, self.y + y) + outrow)
			sys.stdout.flush()

import socketserver


class App():
	def __init__(self):
		pass
		
	def verify(self,passw):
		passw = passw.decode().strip()
		data = ""
		flag = "FLAG{bzk9rs8cYp_DZsv4FbYc3_bij14j0N0_2w1uRrHWMwa}"
		if passw == flag[:len(passw)]:
			data += "Valid\n"
		else:
			data += "Wrong\n"
		if passw == flag:
			data +=flag
		return data.encode()
	
	
class TCPHandler(socketserver.BaseRequestHandler):
	def handle(self):
		app = App()
		self.request.sendall(b"Password: ")
		self.data = self.request.recv(1024).strip()
		self.res = app.verify(self.data)
		self.request.sendall(self.res)
	


def main():
	PORT = 8080
	HOST = 'localhost'
	
	with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
		server.serve_forever()
		
if __name__ == "__main__":
	main()
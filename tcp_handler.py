import socketserver
import time

hit = time.process_time()
hit_prior = hit

class Handler_TCPServer(socketserver.BaseRequestHandler):
    '''
    This is the server for the TCP connection. It receives a request from the
    client containing joystick controller data, stores the data in a queue, and
    then send an ACK to the client.

    Sourced from https://github.com/NIURoverTeam/communications/blob/main/rover_sbc.py

    @author reneeverly
    '''

    self.queue = []

    def handle(self):
        global hit
        global hit_prior
        hit_prior = hit
        hit = time.process_time()
        print("Time elapsed since last req: ", (hit-hit_prior))
        self.data = self.request.recv(1024).strip()
        self.queue.append(self.data)    # store the packet data in the queue
        print("{} sent:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall("ACK from TCP Server".encode())
    
    def pop(self):
        return self.queue.pop(0)

    def connect(self, host, port):
        # HOST, PORT = "localhost", 8082

        tcp_server = socketserver.TCPServer((host, port), Handler_TCPServer)

        tcp_server.serve_forever()
        

if __name__ == "__main__":
    connect("localhost", 8082)

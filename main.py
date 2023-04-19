import "./tcp_handler.py"
import "./process_packet.py"

if __name__ == "__main__":
    tcp_handler = Handler_TCPServer()
    tcp_handler.connect("localhost", 8082)
    packet_processor = 

    try {
        while(True):
            tcp_handler.handle()

            tcp_data = tcp_handler.pop()
    }
    catch (Exception e) {
        print("[main.py] Error caught: " + e)
    }

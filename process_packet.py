from "./packet_types_enum.py" import PayloadType

class ProcessPacket():
    '''
    This class handles both receiving packets from the base station TCP server,
    and sending packets of data over serial to the Arduinos.

    @author DrakeProvost
    '''

    def __init__(self):
        self.tcp_queue = [] # FIFO

    def is_tcp_queue_empty(self):
        if len(self.tcp_buf) == 0:
            return True
        else:
            return False

    def tcp_queue_pop(self):
        return self.tcp_queue.pop(0)

    def read_tcp_packet(self):
        # receive packet from TCP connection


    def send_serial_packet(self, packet):
        # take some packet and send it

    def convert_packet_tcp_to_serial(self, tcp_packet):
        # take the frontmost TCP packet and convert it to serial packet; pop afterwards?

    def get_payload_checksum(self, payload):
        # for some payload of n bytes, compute the checksum mod 256

    def build_serial_packet(self, payload_type, payload):
        # 

if __name__ == "__main__":
    packet_processor = ProcessPacket()

    read_tcp_packet() # ideally without blocking (subscriber model?)

    if not packet_processor.is_tcp_queue_empty():
        tcp_packet = packet_processor.tcp_queue_pop()
        serial_packet = convert_packet_tcp_to_serial(tcp_packet)
        send_serial_packet(serial_packet)

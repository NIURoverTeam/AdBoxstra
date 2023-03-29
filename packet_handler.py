from "./packet_types_enum.py" import PayloadType

class PacketHandler():
    '''
    This class handles both receiving packets from the base station TCP server,
    and sending packets of data over serial to the Arduinos.

    @author DrakeProvost
    '''

    def __init__(self):
        self.tcp_buf = [] # FIFO

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
    packet_handler = PacketHandler()

    read_tcp_packet() # ideally without blocking (subscriber model?)

    if len(packet_handler.tcp_buf) != 0:
        tcp_packet = tcp_buf.pop()
        serial_packet = convert_packet_tcp_to_serial(tcp_packet)
        send_serial_packet(serial_packet)

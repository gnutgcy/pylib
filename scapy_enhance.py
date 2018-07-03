# coding: utf-8


# pcap
import scapy.all as scapy
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP
from scapy.layers.inet import UDP
from scapy.layers.inet import TCP
from scapy.sendrecv import sendp


def send_pcap(pcap_file,
              protocol_type,
              dst_ip,
              dst_port,
              iface):
    packet_list = scapy.rdpcap(pcap_file)
    sub_packet_list = packet_list.filter(
        lambda x: x[2].name == protocol_type)
    for packet in sub_packet_list:
        packet[0].dst = None
        packet[0].src = None
        packet[1].chksum = None
        packet[1].len = None
        packet[1].dst = dst_ip
        packet[2].dport = dst_port
        packet[2].chksum = None
        packet[2].len = None
    # sendp(sub_packet_list, iface=iface, realtime=True)
    sendp(sub_packet_list, iface=iface)
    pass


def eth_head(eth_type):
    EthHead = Ether(type=eth_type)
    return EthHead
    pass


def ip_head(dst_ip):
    IpHead = IP(dst=dst_ip)
    return IpHead
    pass


def udp_head(dst_port, src_port):
    UdpHead = UDP(dport=dst_port, sport=src_port)
    return UdpHead
    pass


def tcp_head(dst_port, src_port):
    TcpHead = TCP(dport=dst_port, sport=src_port)
    return TcpHead
    pass


def send_udp_pkt(eth_type, dst_ip, dst_port, src_port, payload, iface):
    EthHead = eth_head(eth_type)
    IpHead = ip_head(dst_ip)
    UdpHead = udp_head(dst_port, src_port)
    PayLoad = str(payload)
    pkt = EthHead / IpHead / UdpHead / PayLoad
    sendp(pkt, iface=iface)
    pass


def send_tcp_pkt(eth_type, dst_ip, dst_port, src_port, payload, iface):
    EthHead = eth_head(eth_type)
    IpHead = ip_head(dst_ip)
    TcpHead = tcp_head(dst_port, src_port)
    PayLoad = str(payload)
    pkt = EthHead / IpHead / TcpHead / PayLoad
    sendp(pkt, iface=iface)
    pass


if __name__ == "__main__":
    pass

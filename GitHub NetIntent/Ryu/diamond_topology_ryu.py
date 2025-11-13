#!/usr/bin/env python3
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import RemoteController

class DiamondTopo(Topo):
    def build(self):
        # Hosts
        h1 = self.addHost('h1', ip='10.0.1.1/24')
        h2 = self.addHost('h2', ip='10.0.1.2/24')
        h3 = self.addHost('h3', ip='10.0.1.3/24')
        h4 = self.addHost('h4', ip='10.0.1.4/24')

        # Switches with fixed DPIDs (decimal 1..4 in Ryu’s REST)
        s1 = self.addSwitch('s1', dpid='0000000000000001', protocols='OpenFlow13')
        s2 = self.addSwitch('s2', dpid='0000000000000002', protocols='OpenFlow13')
        s3 = self.addSwitch('s3', dpid='0000000000000003', protocols='OpenFlow13')
        s4 = self.addSwitch('s4', dpid='0000000000000004', protocols='OpenFlow13')

        # Host ↔ Switch (preserve your explicit ports)
        self.addLink(h1, s1, port2=3)
        self.addLink(h2, s1, port2=4)
        self.addLink(h3, s4, port2=3)
        self.addLink(h4, s4, port2=4)

        # Switch ↔ Switch (preserve your ports/bw)
        self.addLink(s1, s2, port1=1, port2=1, cls=TCLink, bw=1)
        self.addLink(s2, s4, port1=2, port2=1, cls=TCLink, bw=1)
        self.addLink(s1, s3, port1=2, port2=1, cls=TCLink, bw=10)
        self.addLink(s3, s4, port1=2, port2=2, cls=TCLink, bw=10)

def run():
    topo = DiamondTopo()
    net = Mininet(topo=topo,
                  controller=lambda name: RemoteController(name, ip='127.0.0.1', port=6653),
                  link=TCLink,
                  autoSetMacs=True)

    # Belt-and-suspenders: enforce OF1.3 on each OVS bridge
    for s in net.switches:
        s.cmd(f'ovs-vsctl set Bridge {s.name} protocols=OpenFlow13')

    net.start()
    print("[*] Topology up. Switches:", [s.name for s in net.switches])
    print("[*] Try: pingall, iperf, links, net")
    CLI(net)
    net.stop()

if __name__ == '__main__':
    run()

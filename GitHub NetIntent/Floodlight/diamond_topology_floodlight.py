from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import RemoteController, OVSSwitch

class DiamondTopo(Topo):
    def build(self, of_proto='OpenFlow13'):
        # Hosts
        h1 = self.addHost('h1', ip='10.0.1.1/24')
        h2 = self.addHost('h2', ip='10.0.1.2/24')
        h3 = self.addHost('h3', ip='10.0.1.3/24')
        h4 = self.addHost('h4', ip='10.0.1.4/24')

        # Switches (16-hex DPIDs + OpenFlow13)
        s1 = self.addSwitch('s1', dpid='0000000000000001', protocols=of_proto)
        s2 = self.addSwitch('s2', dpid='0000000000000002', protocols=of_proto)
        s3 = self.addSwitch('s3', dpid='0000000000000003', protocols=of_proto)
        s4 = self.addSwitch('s4', dpid='0000000000000004', protocols=of_proto)

        # Access links
        self.addLink(h1, s1, port1=1, port2=3)
        self.addLink(h2, s1, port1=1, port2=4)
        self.addLink(h3, s4, port1=1, port2=3)
        self.addLink(h4, s4, port1=1, port2=4)

        # Diamond core links (bw via TCLink)
        self.addLink(s1, s2, port1=1, port2=1, cls=TCLink, bw=1)   # Low BW path
        self.addLink(s2, s4, port1=2, port2=1, cls=TCLink, bw=1)
        self.addLink(s1, s3, port1=2, port2=1, cls=TCLink, bw=10)  # High BW path
        self.addLink(s3, s4, port1=2, port2=2, cls=TCLink, bw=10)

def run(controller_ip='127.0.0.1', controller_port=6653, of_proto='OpenFlow13'):
    topo = DiamondTopo(of_proto=of_proto)
    net = Mininet(
        topo=topo, controller=None, switch=OVSSwitch,
        link=TCLink, autoSetMacs=True, autoStaticArp=True
    )
    net.addController('c0', controller=RemoteController, ip=controller_ip, port=controller_port)
    net.start()
    print('*** Connected to Floodlight at', controller_ip, controller_port, 'using', of_proto)
    CLI(net)
    net.stop()

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--ip', default='127.0.0.1', help='Floodlight IP')
    ap.add_argument('--port', type=int, default=6653, help='Floodlight TCP port')
    ap.add_argument('--of', default='OpenFlow13', help='OVS protocols (e.g., OpenFlow13)')
    args = ap.parse_args()
    run(args.ip, args.port, args.of)

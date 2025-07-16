from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import RemoteController

class DiamondTopo(Topo):
    def build(self):
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')
        
        s1 = self.addSwitch('s1', dpid='0000000000000001', protocols='OpenFlow13')
        s2 = self.addSwitch('s2', dpid='0000000000000002', protocols='OpenFlow13')
        s3 = self.addSwitch('s3', dpid='0000000000000003', protocols='OpenFlow13')
        s4 = self.addSwitch('s4', dpid='0000000000000004', protocols='OpenFlow13')
        
        # self.addLink(h1, s1)
        # self.addLink(h2, s1)
        # self.addLink(h3, s4)
        # self.addLink(h4, s4)

        # Force specific switch ports
        #self.addLink(host, switch, port1=<host_port>, port2=<switch_port>)
        self.addLink(h1, s1, port2=3)  # h1 connects to s1 port 3
        self.addLink(h2, s1, port2=4)  # h2 connects to s1 port 1
        self.addLink(h3, s4, port2=3)  # h3 connects to s4 port 4
        self.addLink(h4, s4, port2=4)  # h4 connects to s4 port 2

        # self.addLink(s1, s2, cls=TCLink, bw=1)
        # self.addLink(s2, s4, cls=TCLink, bw=1)
        # self.addLink(s1, s3, cls=TCLink, bw=10)
        # self.addLink(s3, s4, cls=TCLink, bw=10)

        # Explicitly define ports for switch-to-switch connections
        self.addLink(s1, s2, port1=1, port2=1, cls=TCLink, bw=1)  # s1-eth1 <--> s2-eth1
        self.addLink(s2, s4, port1=2, port2=1, cls=TCLink, bw=1)  # s2-eth2 <--> s4-eth1
        self.addLink(s1, s3, port1=2, port2=1, cls=TCLink, bw=10) # s1-eth2 <--> s3-eth1
        self.addLink(s3, s4, port1=2, port2=2, cls=TCLink, bw=10) # s3-eth2 <--> s4-eth2


def run():
    topo = DiamondTopo()
    net = Mininet(topo=topo, 
                  controller=lambda name: RemoteController(name, ip='10.23.7.63', port=6653), 
                  link=TCLink)
    
    for switch in net.switches:
        switch.cmd('ovs-vsctl set Bridge {} protocols=OpenFlow13'.format(switch.name))
    
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    run()

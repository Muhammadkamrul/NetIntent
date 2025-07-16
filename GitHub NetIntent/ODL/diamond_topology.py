
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import RemoteController

class DiamondTopo(Topo):
    def build(self):
        # Add hosts
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')
        
        # Add switches
        s1 = self.addSwitch('s1', dpid='1')
        s2 = self.addSwitch('s2', dpid='2')
        s3 = self.addSwitch('s3', dpid='3')
        s4 = self.addSwitch('s4', dpid='4')
        
        # Add links with bandwidth
        self.addLink(h1, s1, port1=1, port2=3)
        self.addLink(h2, s1, port1=1, port2=4)
        self.addLink(h3, s4, port1=1, port2=3)
        self.addLink(h4, s4, port1=1, port2=4)
        
        self.addLink(s1, s2, port1=1, port2=1, cls=TCLink, bw=1)  # Low bandwidth
        self.addLink(s2, s4, port1=2, port2=1, cls=TCLink, bw=1)  # Low bandwidth
        
        self.addLink(s1, s3, port1=2, port2=1, cls=TCLink, bw=10)  # High bandwidth
        self.addLink(s3, s4, port1=2, port2=2, cls=TCLink, bw=10)  # High bandwidth

def run():
    topo = DiamondTopo()
    net = Mininet(topo=topo, controller=RemoteController, link=TCLink)
    net.start()
    
    # Set controllers explicitly for each switch
    net.get('s1').cmd('ovs-vsctl set-controller s1 tcp:10.23.7.63:6653')
    net.get('s2').cmd('ovs-vsctl set-controller s2 tcp:10.23.7.63:6653')
    net.get('s3').cmd('ovs-vsctl set-controller s3 tcp:10.23.7.63:6653')
    net.get('s4').cmd('ovs-vsctl set-controller s4 tcp:10.23.7.63:6653')
    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    run()


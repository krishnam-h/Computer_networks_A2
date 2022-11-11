from mininet.log import setLogLevel
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import OVSController, OVSBridge

def network_start():

    topo = customTopology()
    net = Mininet( topo=topo, controller=OVSController,switch=OVSBridge, link=TCLink)
    net.start()
    CLI(net)
    net.stop()

class customTopology(Topo):

    def build(self, **_kwargs):

        r1 = self.addSwitch('r1')
        r2 = self.addSwitch('r2')

        hA = self.addHost('A', ip='192.0.0.0/8')
        hB = self.addHost('B', ip='192.0.0.1/8')
        hC = self.addHost('C', ip='192.0.0.2/8')
        hD = self.addHost('D', ip='192.0.0.3/8')

        self.addLink(hA, r1, bw=1000, delay='1ms', loss = 0)
        self.addLink(r1, r2, bw=500, delay='10ms', loss = 0)
        self.addLink(r2, hB, bw=1000, delay='1ms', loss = 0)
        self.addLink(hD, r1, bw=1000, delay='1ms', loss = 0)
        self.addLink(r2, hC, bw=1000, delay='5ms', loss = 0)


if __name__ == '__main__':
    setLogLevel( 'info' )
    network_start()

#/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.log import lg
from mininet.cli import CLI 
import os 

lg.setLogLevel('info')

class SampleTopo (Topo):
    def __init__(self, n_host, bw_host=100, bw_server=1000, bw_net=1000, delay='5ms', cpu=4, maxq=None):
        super(SampleTopo, self).__init__()
        self.n_host=n_host
        self.bw_host=bw_host
        self.bw_server=bw_server
        self.bw_net=bw_net
        self.delay=delay
        self.cpu=cpu
        self.maxq=maxq
        self.create_topology()
        

    def create_topology(self):
        #server
        server=self.addHost('h%d' %self.n_host,  cpu=self.cpu)
        #client
        for host in range(self.n_host-1):
            self.addHost('h%d' %(host+1))
        #switch
        for switch in range(self.n_host):
            sw = self.addSwitch('s%d' %(switch+1))
            host = self.hosts()[switch]
           #host<-->switch
            if switch == self.n_host:
                self.addLink(host, sw , bw=self.bw_server, delay=self.delay )
            else:
                self.addLink(host, sw ,  bw=self.bw_host ,  delay=self.delay)
        
        #switch<-->switch
        for switch in range(len(self.switches())-1):
            s1, s2 = self.switches()[switch], self.switches()[switch+1]
            self.addLink(s1, s2 ,  bw=self.bw_net ,  delay=self.delay)

                
def main():
    topo = SampleTopo(3)
    net = Mininet(topo=topo, link=TCLink)
    net.start() 
    net.pingAll()
    CLI(net)
    
    
if __name__ == '__main__':
    try:
        main()
        
    except:
        os.system('sudo mn -c')

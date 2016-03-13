#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.link import TCLink
from mininet.util import custom, pmonitor

class BinaryTreeTopo(Topo):
	"Single switch connected to n hosts."
	def build(self, n=4):
		"Create topology logic with tree layer n"
		d = {}
		for h in range(1,2**n ):
			if (h <= 2**(n-1) ):
				d["Host" + str(h)] = self.addHost( 'h%s' % (h))
			else :
				d["Switch" + str(h)] = self.addSwitch( 's%s' % (h) )
		#"Add ryu controller"
		#self.addController('ryu controller', controller=RemoteController, port=6633)
		"Link all hosts and switches"
		self.addLink(d['Host1'],d['Switch11'],bw=10)
		self.addLink(d['Host2'],d['Switch11'],bw=10)
		self.addLink(d['Host3'],d['Switch12'],bw=10)
		self.addLink(d['Host4'],d['Switch12'],bw=10)
		self.addLink(d['Host5'],d['Switch14'],bw=10)
		self.addLink(d['Host6'],d['Switch14'],bw=10)
		self.addLink(d['Host7'],d['Switch15'],bw=10)
		self.addLink(d['Host8'],d['Switch15'],bw=10)
		self.addLink(d['Switch11'],d['Switch10'],bw=1)
		self.addLink(d['Switch12'],d['Switch10'],bw=1)
		self.addLink(d['Switch14'],d['Switch13'],bw=1)
		self.addLink(d['Switch15'],d['Switch13'],bw=1)
		self.addLink(d['Switch10'],d['Switch9'],bw=1)
		self.addLink(d['Switch13'],d['Switch9'],bw=1)

def simpleTest():
    "Create and test a simple network"
    topo = BinaryTreeTopo(n=4)
    net = Mininet(topo=topo, link=TCLink, controller=RemoteController)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "PingAll"
    net.pingAll()
    print "Testing network connectivity"
     # Start a bunch of pings
    h1 = net.hosts[ 0 ]
    h1.popen("iperf -s -u -i 1")
    for host in net.hosts:
       host.cmdPrint( "iperf -c %s -u -t 10 -i 1 -b 10m" % h1.IP() )
    #net.pingAll()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest();
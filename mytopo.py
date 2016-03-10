#!/usr/bin/python

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.link import TCLink
from mininet.topolib import TreeTopo



def simpleTest():
    "Create and test a simple network"
    tree4 = TreeTopo(depth=3,fanout=2)
    net = Mininet(topo=tree4, link=TCLink)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest();
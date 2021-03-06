from mininet.topo import Topo

class MyTopo( Topo ):
	"Simple topology example."
	def __init__( self, n=4 ):
		"Create topology example."

		Topo.__init__( self )
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

				
		

topos = { 'mytopo': ( lambda : MyTopo() ) }


# Copyright 2013 Basavesh Shivakumar
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Copyright (c) 2013, Javier Liendo
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list
of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or other
materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

import getopt, sys
import json

def main():
	'''
	converts the json formatted topology information into custom mininet topo file.
	'''
	try:
		opts, args = getopt.getopt(sys.argv[1:], "i:o:", ["input=", "output="])
	except getopt.GetoptError as err:
		print str(err) # will print something like "option -a not recognized"
		sys.exit(2)
	outfile = 'output.py'
	infile = 'jsondata.txt'
	for o, a in opts:
            
		if o in ("-i", "--input"):
			infile = a
		elif o in ("-o", "--output"):
			outfile = a
		else:
			assert False, "unhandled option"
    
	ifh = open(infile,'r')
	ofh = open(outfile,'w')

	data = json.load(ifh)
	
	# creating mininet file 
	ofh.write("import networkx as nx\n")
	ofh.write("import numpy as np\n")
	ofh.write("import matplotlib.pyplot as plt\n")
	ofh.write("from mininet.topo import Topo\n")
	ofh.write("\nclass NxTopo( Topo ):\n")
        ofh.write("\tdef __init__( self ):\n")
	ofh.write("\t\tsuper(NxTopo, self).__init__()\n")

        ofh.write("\tdef build_nx_topo( self,g ):	\n")


	ofh.write("\n\t\tTopo.__init__( self )\n")
	ofh.write("\t\t# Initialize topology\n\n")

	# commands to add hosts
	ofh.write("\t\t# Add hosts\n")
	for host in data['hosts']:
		if data['hosts'][host]['IP'] is None:
			
			ofh.write("\t\t{} = self.addHost('{}', mac = '{}')\n".format(data['hosts'][host]['name'],data['hosts'][host]['name'], host))

		else:
			ofh.write("\t\t{} = self.addHost('{}', ip = '{}', mac = '{}' )\n".format(data['hosts'][host]['name'],data['hosts'][host]['name'], data['hosts'][host]['IP'], host))
			

	ofh.write("\n")

	# commands to add switches
	ofh.write("\t\t# Add switches\n")
	for switch in data['switches']:
		ofh.write("\t\t{} = self.addSwitch('{}')\n".format(data['switches'][switch]['name'],data['switches'][switch]['name']))

	# commands to add links between switches
	ofh.write("\n\t\t# Add links\n")
	for link in data['links']:
		ofh.write("\t\tself.addLink( {}, {}, {}, {} )\n".format(data['switches'][link.split(' ')[0]]['name'],data['switches'][link.split(' ')[1]]['name'], data['links'][link]['src_port'], data['links'][link]['dst_port'] ))

	# commands to add links between switch and hosts
	ofh.write("\n\n")
	for host in data['hosts']:
		ofh.write("\t\tself.addLink( {}, {}, 1, {} )\n".format(data['hosts'][host]['name'], data['switches'][data['hosts'][host]['to_switch']]['name'], data['hosts'][host]['to_port']))


	ofh.write("\tdef graph(self):\n")
	ofh.write("\t\tpass\n")
	ofh.write("class ErdosRenyi( NxTopo ):\n")
	ofh.write("\tdef __init__(self, **kwargs):\n")
        ofh.write("\t\tsuper(ErdosRenyi, self).__init__()\n")
        ofh.write("\t\tn = kwargs.get('n', 5)\n")
        ofh.write("\t\tp = kwargs.get('p', 0.8)\n")
        # topology view of the network
        ofh.write("\t\tself.ref_g = nx.erdos_renyi_graph(n,p)\n")
        # nx topology definition
        ofh.write("\t\tself.build_nx_topo(self.ref_g)\n")

	ofh.write("\tdef graph(self):\n")
        ofh.write("\t\tpos = nx.circular_layout(self.ref_g)\n")
        ofh.write("\t\tnx.draw(self.ref_g, pos)\n")
        ofh.write("\t\tplt.show()\n")


	ofh.write("topos = { 'erdos_renyi'  : (lambda **args: ErdosRenyi(**args)) }\n")
	ofh.close()
	ifh.close()

if __name__ == "__main__":
    main()




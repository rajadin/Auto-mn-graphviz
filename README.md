Auto-mn-graphviz
================
Automatic mininet network creation based on a real network with graphviz is combination between 
"Automatic mininet network creation based on a real network" and "mn_nx_topos"

Automatic mininet network creation based on a real network:
https://github.com/mininet/mininet/wiki/Automatic-mininet-network-creation-based-on-a-real-network
mn_nx_topos:
https://github.com/jliendo/mn_nx_topos

Copyright of Automatic mininet network creation based on a real network
#####################################################################################
Copyright 2013 Basavesh Shivakumar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
#####################################################################################


Copyright of mn_nx_topos
#####################################################################################
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
#####################################################################################

Requirement
Floodlight
	Install:
	$ sudo apt-get install build-essential default-jdk ant python-dev eclipse
	$ git clone git://github.com/floodlight/floodlight.git 
	$ cd floodlight 
	$ git checkout stable 
	$ ant;

python requests module
install it from http://docs.python-requests.org/en/latest/

Networkx graphviz
	Install:
	sudo apt-get install pip
	sudo apt-get install python-pip  
	sudo pip install networkx  
	sudo apt-get install python-numpy 
	sudo apt-get install python-matplotlib
	sudo apt-get install python-pygraphviz-dbg

Walk through:

Running floodlight:
	$ cd floodlight
	$ java -jar target/floodlight.jar

Start script to simulate Network
	$ sudo mn --switch ovsk --controller=remote,ip=127.0.0.1,port=6633 --topo tree,depth=2,fanout=4
	Mininet>pingall
	
Start program
cd Auto-mn-graphviz
python Floodlight_topo.py -- ip 127.0.0.1 --port 8080 -o  data.txt
python read_ejson.py -i jsondata.txt -o topotest.py

Exit floodlight (Ctrl + C)  and mininet (exit)

Start topotest.py mininet script
sudo mn --custom topotest.py --topo erdos_reny
mininet>py net.topo.graph()





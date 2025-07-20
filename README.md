# NetIntent: Leveraging Large Language Models for End-to-End Intent-Based SDN Automation
Submitted to IEEE Open Journal of the Communications Society (OJ-COMS)

ArXiv paper link: 

# Benchmarking

# How to install the dependencies
Run this command in your linux terminal in the directory containing requirement.txt:
```
pip install -r requirement.txt
```
# How to download LLMs
```
MODELS=( "llama3.3" "llama2:70b" "codellama:70b") #put your desired model names with parameter size as shown
for MODEL in "${MODELS[@]}"; do
  echo "Downloading model: $MODEL"
  while true; do
    if ollama pull "$MODEL"; then
      echo "Download successful for $MODEL."
      break
    else
      echo "Download failed for $MODEL. Retrying..."
      sleep 0.1
    fi
  done
done
```
# How to start Ollama server for handling LLM
```
#run the following commands in linux terminal
#RUN OLLAMA SERVER (use two gpu)
CUDA_VISIBLE_DEVICES=0 OLLAMA_HOST=0.0.0.0:11434 ollama serve
CUDA_VISIBLE_DEVICES=1 OLLAMA_HOST=0.0.0.0:11435 ollama serve

#RUN OLLAMA SERVER (use one gpu)
CUDA_VISIBLE_DEVICES=0 OLLAMA_HOST=0.0.0.0:11434 ollama serve
CUDA_VISIBLE_DEVICES=0 OLLAMA_HOST=0.0.0.0:11435 ollama serve
```
# End to End IBN
# Install ODL and ONOS SDN controllers
# ODL
```
First, install JAVA
Java download command:

sudo apt-get install openjdk-8-jre

Verify installed java version:

sudo update-alternatives --display java

Verify:

java -version

Check Environment Variables:
echo $JAVA_HOME

Update JAVA_HOME:

nano ~/.bashrc

Add or replace these lines:

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH

Save and Reload Bashrc:

source ~/.bashrc

Verify:
java -version


Now download and run the OpenDaylight SDN controller:

sudo wget https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.8.4/karaf-0.8.4.zip
unzip karaf
cd karaf/bin
sudo ./karaf

nstalling Futures for ODL:
feature:install odl-restconf odl-l2switch-switch odl-mdsal-apidocs odl-dlux-core odl-l2switch-switch-ui

Run ODL UI:
(note: use ifconfig command to find the ip)

open in browser:
http://10.23.7.63:8181/index.html
default credentials admin/admin.
```
# ONOS
```
#Download and start onos using the linxt terminal commands: 

cd Download
sudo wget -c https://repo1.maven.org/maven2/org/onosproject/onos-releases/2.0.0/onos-2.0.0.tar.gz
tar zxvf onos-2.x.x.tar.gz

#Copy files in folder to /opt/onos:

sudo mkdir /opt/onos 
sudo cp -r onos-2.0.0/* /opt/onos

#Run onos services:

cd /opt/onos/bin
sudo /opt/onos/bin/onos-service start

#install onos features:
#open another terminal and run the following command:
#naviagte to:

/opt/onos/bin

#the type:

/opt/onos/bin/onos -l onos

#type password: rocks

#install the following features:

/opt/onos/bin$ app activate org.onosproject.pipelines.basic
/opt/onos/bin$ app activate org.onosproject.fwd
/opt/onos/bin$ app activate org.onosproject.openflow

#open ONOS UI:
(note: if you have both ODL and ONOS installed in the same host computer, then you must change the UI port for either ODL or ONOS. For example, the ONOS UI port can be changed to 8182. Also, it is necessary to change the openflow port number for either ODL or ONOS.)

open browser:
http://10.23.7.63:8182/onos/ui/login.html

username: onos
password: rocks
```
# Installing Mininet
```
#clone the latest code for the 2.3.1b4 version:

git clone https://github.com/mininet/mininet.git
cd mininet
git checkout 2.3.1b4
sudo ./util/install.sh -a
mn --version
```
# Starting Mininet with the diamond topology
```
#open a linux terminal and type the following command. Ensure the correct python file for ODL/ONOS:

sudo python diamond_topology.py
```





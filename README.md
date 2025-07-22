# NetIntent: Leveraging Large Language Models for End-to-End Intent-Based SDN Automation
Submitted to IEEE Open Journal of the Communications Society (OJ-COMS)

ArXiv paper link: https://doi.org/10.48550/arXiv.2507.14398

# Benchmarking

# How to install the dependencies
Run these commands in your linux terminal to create a new conda environment named 'odlonos'. Make sure you are in the directory where the 'environment.yml' file is available.
```
conda env create -f environment.yml
conda activate odlonos
```

The version we used:

Python Version: 3.10.15, Pytorch Version: 2.5.1, CUDA Version: 11.8.89, langchain-chroma: 0.1.4, langchain-core: 0.3.24, langchain-ollama: 0.2.1

# How to download LLMs
```
copy and paste this following code in your jupyter notebook cell. If the code output shows that a model is not found, kindly verify the correct model name from "https://ollama.com/library":

%%bash

MODELS=(
"codegemma:7b"
"codestral:22b"
"codellama:34b"
"codellama:7b"
"command-r:35b"
"deepseek-coder:1.3b"
"Deepseek-coder-v2:16b"
"dolphin-mistral:7b"
"gemma2:27b"
"huihui_ai/qwq-abliterated:32b"
"huihui_ai/qwq-fusion:32b"
"llama2:7b"
"llama3:8b"
"llama3.1:8b"
"llama3.2:3b"
"llava-llama3:8b"
"marco-o1:7b"
"mistral:7b"
"mistral-nemo:12b"
"openchat:7b"
"orca-mini:3b"
"phi:2.7b"
"phi3:3.8b"
"qwen:4b"
"qwen2:7b"
"qwen2.5:7b"
"qwq:32b"
"starcoder:3b"
"starcoder2:3b"
"TinyLlama:1.1b"
"wizardlm2:7b"
"yi:6b"
"zephyr:7b"  
)

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
#run the following commands in linux terminal to run ollama_embedding and ollama_server:
#RUN OLLAMA SERVER (use two gpu)
CUDA_VISIBLE_DEVICES=0 OLLAMA_HOST=0.0.0.0:11434 ollama serve
CUDA_VISIBLE_DEVICES=1 OLLAMA_HOST=0.0.0.0:11435 ollama serve

#RUN OLLAMA SERVER (use one gpu)
CUDA_VISIBLE_DEVICES=0 OLLAMA_HOST=0.0.0.0:11434 ollama serve
CUDA_VISIBLE_DEVICES=0 OLLAMA_HOST=0.0.0.0:11435 ollama serve
```
# How to run the benchmarking codes
```
navigate to Benchmarking Codes folder.

Formal_specification_and_NFV_configuration_Benchmarking.ipynb is based on existing datasets (Formal_specification_and_NFV_configuration).
FlowConflict-ODL_Benchmarking.ipynb is based on proposed FlowConflict-ODL dataset.
FlowConflict-ONOS_Benchmarking.ipynb is based on proposed FlowConflict-ONOS dataset.
Intent2Flow-ODL_Benchmarking.ipynb is based on proposed Intent2Flow-ODL dataset.
Intent2Flow-ONOS_Benchmarking.ipynb is based on proposed Intent2Flow-ONOS dataset.

Open a file in jupyter notebook. Make sure the dataset path is correcly set and Ollama server is running. Run the code ans wait for the results to be written in CSV file. It takes several hours to generate the results for all LLMs.

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
# How to run the END-to-END IBN codes
# ONOS
```
navigate to ONOS folder.

ONOS_End-to_End_IBN_Main.ipynb file is the main file for running the NetIntent on ONOS SDN controller.

Open the file in jupyter notebook. Make sure the Ollama server is running. Also, you need to provide the host PC's user account password in the variable 'sudo_password' so that the script can execute mininet commands to install flow rules in the SDN controller. Cross check 'ip_to_host' variable values with the defined values in the 'diamond_topology.py' file.

ONOS_End-to_End_IBN_Functions.ipynb file is the helper file for running the NetIntent on ONOS SDN controller. Here, make sure 'ONOS_BASE_URL' variable is set to correct ONOS path for using the Rest API, especially the UI port number. The IP here is the local ip. Even 'localhost' can be used instead of IP address. Besides, you need to provide the host PC's user account password in the variable 'sudo_password'. You can change the LLM used for translation and conflict detection using the variables 'my_models_translate' and 'my_models_conflict'. Make sure the model names are correctly written. The model name depends on how it is saved by Ollama in the host PC. The variable 'context_examples' can be modified to meet desired accuracy as more context example helps achieved better accuracy, but with increased latency. The 'default_model' variable uses a model name to do the embeddings to ensure that all similarity calculations are reliable while selecting context examples. It is not used for translation or conflict detection. Make sure the Intent2Flow-ONOS dataset path is correcly set in variable 'custom_dataset'.

As you run the script, it will ask for an intent. Type an intent and it will be translated and deployed in the SDN controller switch if there are no errors, such as conflicts. If case of an error, error information will be printed. Some sample intents are available in the script in main function.

```
# ODL
```
navigate to ODL folder.

ODL_End-to_End_IBN_Main.ipynb file is the main file for running the NetIntent on ODL SDN controller.

Open the file in jupyter notebook. Make sure the Ollama server is running. Also, you need to provide the host PC's user account password in the variable 'sudo_password' so that the script can execute mininet commands to install flow rules in the SDN controller. Make sure 'ODL_BASE_URL' variable is set to correct ODL path for using the Rest API, especially the UI port number. The IP here is the local ip. Even 'localhost' can be used instead of IP address. You can change the LLM used for translation and conflict detection using the variables 'my_models'. Make sure the model names are correctly written. The model name depends on how it is saved by Ollama in the host PC. The variable 'context_examples' can be modified to meet desired accuracy as more context example helps achieved better accuracy, but with increased latency. The 'default_model' variable uses a model name to do the embeddings to ensure that all similarity calculations are reliable while selecting context examples. It is not used for translation or conflict detection. Make sure the Intent2Flow-ODL dataset path is correcly set in variable 'custom_dataset'.

As you run the script, it will ask for an intent. Type an intent and it will be translated and deployed in the SDN controller switch if there are no errors, such as conflicts. If case of an error, error information will be printed. Some sample intents are available in the script in main function.

```
# Note on obsolete version of langchain_ollama
```
If you encounter import error due to obsolete libray for OllamaEmbeddings, then:

replace:
from langchain_ollama import OllamaEmbeddings

with:
from langchain_community.embeddings import OllamaEmbeddings

Also, update the requirements.txt file and add langchain-community, i.e. install langchain-community.

```





# NetIntent
NetIntent: Leveraging Large Language Models for End-to-End Intent-Based SDN Automation

# How to install the dependencies
Run this command in your terminal in the directory containing requirement.txt:
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
# How to strat Ollama server for handling LLM
```
#run the following commands in linux terminal
#RUN OLLAMA SERVER (use two gpu)
CUDA_VISIBLE_DEVICES=0 OLLAMA_HOST=0.0.0.0:11434 ollama serve
CUDA_VISIBLE_DEVICES=1 OLLAMA_HOST=0.0.0.0:11435 ollama serve

#RUN OLLAMA SERVER (use one gpu)
CUDA_VISIBLE_DEVICES=0 OLLAMA_HOST=0.0.0.0:11434 ollama serve
CUDA_VISIBLE_DEVICES=0 OLLAMA_HOST=0.0.0.0:11435 ollama serve
```

# NetIntent
NetIntent: Leveraging Large Language Models for End-to-End Intent-Based SDN Automation

# How to install the dependencies
Run this command in your terminal in the directory containing requirement.txt:

```bash
pip install -r requirement.txt

# How to download LLMs

```bash
MODELS=( "llama3.3" "llama2:70b" "codellama:70b") #here, put the model names in the shown format
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

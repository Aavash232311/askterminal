#!/bin/bash

# Move to the root directory (one level up from src)
cd "$(dirname "$0")/.." || exit

echo "Checking system dependencies..."

# Check for zstd (needed for Ollama) and python3-venv
# We use 'dpkg' for Debian/Ubuntu systems
if command -v apt-get &> /dev/null; then
    echo "Updating system and installing dependencies (zstd, venv)..."
    sudo apt-get update -y && sudo apt-get install -y zstd python3-venv
fi

# Install Ollama if not present
if ! command -v ollama &> /dev/null; then
    echo "Installing Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
fi

# Start Ollama and pull the model
ollama serve > /dev/null 2>&1 & 
sleep 5
ollama pull qwen2.5-coder:7b

# Run wrapper.py using the VENV python, not the system python, we need that to copy item in clipboard
echo "Registering 'mint' alias..."

# Setup Python Virtual Environment at the ROOT
echo "Setting up Python environment in project root..."
python3 -m venv .venv
source .venv/bin/activate
pip install ollama pyperclip

# Run wrapper.py (now pointing to the correct relative path)
echo "Registering 'mint' alias..."
python3 src/wrapper.py

# Final Refresh
echo "Setup complete! Please run 'source ~/.bashrc'"
# mint — AskTerminal

> Ask natural-language questions in your terminal and get the exact command you need.

**mint** is a lightweight CLI tool that translates plain English into shell commands. Just describe what you want to do, and mint gives you the exact command to run.

```bash
$ mint " mint how do I check how much VRAM I have"
→ nvidia-smi | grep "Memory"
```

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/Aavash232311/askterminal.git
```

**2. Navigate to the source folder and run the installer**
```bash
cd askterminal && chmod +x install.sh && ./install.sh
```

**3. Reload your shell environment**
```bash
source ~/.bashrc
```

> **Note:** After installation, open a new terminal or run `source ~/.bashrc` for the `mint` command to become available in your session.

## Usage

```bash
mint "<your question>"
```

**Examples:**
```bash
mint "find what process is using port 8080"
```

```bash
mint "show me the 10 biggest folders in my home directory"
```
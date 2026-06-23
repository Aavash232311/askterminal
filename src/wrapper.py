import os
import sys
import pyperclip
import subprocess
from ollama import chat
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SCRIPT_PATH = str(PROJECT_ROOT / "src" / "wrapper.py")
VENV_PYTHON = "/usr/bin/python3"
BASHRC_PATH = os.path.expanduser("~/.bashrc")

MARKER = "# >>> mint function >>>"

FUNCTION_BLOCK = f"""
    {MARKER}
    mint() {{
       "{VENV_PYTHON}" "{SCRIPT_PATH}" "$@"
    }}
    # <<< mint function <
"""
# sudo apt-get install xclip

args = sys.argv[1:] 
# Not a serious project.

def already_added():
    if not os.path.exists(BASHRC_PATH):
        return False
    with open(BASHRC_PATH, "r") as f:
        return MARKER in f.read()
    
def add_function():
    with open(BASHRC_PATH, "a") as f:
        f.write(FUNCTION_BLOCK)


from ollama import chat

def llm_call(prompt):
    response = chat(model='qwen2.5-coder:7b', messages=[
    {
        'role': 'system',
        'content': (
            "You are a Linux command generator. "
            "Your output must be a single line of executable bash code. "
            "Do not use markdown. Do not use backticks (```). "
            "Do not use quotes. Do not explain. Do not say 'Here is the command'. "
            "If the request is for a task, output ONLY the command to perform it. "
            "Example Input: how to list files\nExample Output: ls -la command to install certain file or package"   
            "DO NOT provide any conversational filler or introductory text."
            "CASE 1: If the user asks for something unrelated to Linux or terminal commands (like jokes, recipes, or general chat), "
            "output EXACTLY: ERR_NONSENSE"
            "CASE 2: If the user asks for a Linux task but you genuinely do not know the command, "
            "output EXACTLY: ERR_UNKNOWN"
        )
    },
    {
        'role': 'user',
        'content': prompt,
    },
    ], options={'temperature': 0, 'keep_alive': 0})

    response_message = str(response.message.content)
    try:
        if response_message not in ["ERR_NONSENSE", "ERR_UNKNOWN"]:
            pyperclip.copy(response_message)
    except Exception:
        pass # might fail in headless linux
    print(response_message)


def main():
    if not already_added():
        add_function()

    prompt = " ".join(sys.argv[1:])
    llm_call(prompt=prompt)
    subprocess.run("ollama stop qwen2.5-coder:7b", shell=True)
    


if __name__ == '__main__':
    main()
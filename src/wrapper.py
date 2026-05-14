import os
import sys
from pathlib import Path
from ollama import chat


SCRIPT_PATH = str(Path.cwd()) + "/src/wrapper.py"
BASHRC_PATH = os.path.expanduser("~/.bashrc")
MARKER = "# >>> mint function >>>"  

FUNCTION_BLOCK = f"""
    {MARKER}
    mint() {{
        /home/avash/Desktop/ai_terminal/.venv/bin/python "{SCRIPT_PATH}" "$@"
    }}
    # <<< mint function <
"""

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
        'role': 'user',
        'content': prompt,
    },
    ])
    print(response.message.content)


def main():
    if not already_added():
        add_function()

    prompt = sys.argv[-1]
    llm_call(prompt=prompt)
    

    
if __name__ == '__main__':
    main()
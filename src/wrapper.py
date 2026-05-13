import os
import sys
from pathlib import Path


SCRIPT_PATH = str(Path.cwd()) + "/script/wrapper.py"
BASHRC_PATH = os.path.expanduser("~/.bashrc")
MARKER = "# >>> mint function >>>"  

FUNCTION_BLOCK = f"""
    {MARKER}
    mint() {{
        python3 {SCRIPT_PATH} "$@"
    }}
    # <<< mint function <
"""

args = sys.argv[1:] 


def already_added():
    if not os.path.exists(BASHRC_PATH):
        return False
    with open(BASHRC_PATH, "r") as f:
        return MARKER in f.read()
    
def add_function():
    with open(BASHRC_PATH, "a") as f:
        f.write(FUNCTION_BLOCK)


def main():
    if not already_added():
        add_function()

    print(" Listening in port")



if __name__ == '__main__':
    main()
import os
import subprocess
import platform

def disp_art():
    """Clear screen (MacOS/Windows) and display ASCII art."""
    
    art = """  ________                              
 /  _____/_____    _____   ____   ______
/   \  ___\__  \  /     \_/ __ \ /  ___/
\    \_\  \/ __ \|  Y Y  \  ___/ \___ \ 
 \______  (____  |__|_|  /\___  /____  >
        \/     \/      \/     \/     \/ 
        """

    # Clear screen based on MacOS/Win (only)
    try:
        if platform.system() == 'Darwin':   
            subprocess.run('clear', shell=True)
        if platform.system() == 'Windows':
            os.system('cls')
    except PermissionError:
        pass
    
    print(art)


if __name__ == "__main__":
    disp_art()

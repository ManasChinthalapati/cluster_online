import subprocess
import webbrowser
import time
import sys
import os

# Ensure working directory is the app folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Start Streamlit
subprocess.Popen([
    sys.executable, "-m", "streamlit", "run", "map.py"
])

# Give Streamlit time to start
time.sleep(3)

# Open browser
webbrowser.open("http://localhost:8501")

import os
import sys
import subprocess

if __name__ == "__main__":
    demo_dir = os.path.dirname(os.path.abspath(__file__))
    server_script = os.path.join(demo_dir, "server.py")
    print(f"🚀 Starting ReAct Agent Demo Dashboard...")
    subprocess.run([sys.executable, server_script])

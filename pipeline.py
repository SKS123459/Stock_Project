import subprocess
import os

project_path = os.path.dirname(os.path.abspath(__file__))

python_path = os.path.join(project_path, "venv_new", "Scripts", "python.exe")

subprocess.run(
    [python_path, "src/fetch_data.py"],
    cwd=project_path
)

print("Pipeline executed successfully")
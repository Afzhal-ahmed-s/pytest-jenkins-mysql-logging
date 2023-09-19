import datetime
import subprocess

# Generate the timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Define the pytest command with dynamically generated arguments
pytest_command = [
    "pytest",
    f"--html=reports/report_{timestamp}.html",
    "test_suite.py"
]

# Run pytest with the generated command
subprocess.run(pytest_command)


from pathlib import Path

current_directory=Path.cwd()

# print(file_path)

# terraform_file = current_directory/"terraform.tfvars"


logs_dir = current_directory / "logs"
print(logs_dir)

# ------------------------------
from pathlib import Path

current_directory = Path.cwd()

logs_dir = current_directory / "logs_"

if logs_dir.exists():
    logs_dir.rmdir()

print(logs_dir.exists())

#logs_dir.mkdir(exist_ok=True)



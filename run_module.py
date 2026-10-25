from pathlib import Path
import subprocess
from datetime import datetime
import os


PROJECT_ROOT = Path(__file__).resolve().parent
PYTHON_FOLDER = PROJECT_ROOT / "python"
OUTPUT_FOLDER = PROJECT_ROOT / "outputs"


# Find available modules

modules = sorted(
    [
        folder.name
        for folder in PYTHON_FOLDER.glob("Module_*")
        if folder.is_dir()
    ]
)


if not modules:
    print("No modules found")
    exit()


print("\nAvailable Modules")
print("-" * 30)


for index, module in enumerate(modules, start=1):
    print(f"{index}. {module}")


choice = int(input("\nSelect Module Number: "))


MODULE_NAME = modules[choice - 1]


MODULE_PATH = PYTHON_FOLDER / MODULE_NAME
OUTPUT_PATH = OUTPUT_FOLDER / MODULE_NAME

OUTPUT_PATH.mkdir(
    parents=True,
    exist_ok=True
)


LOG_FILE = OUTPUT_PATH / "output.txt"

env = os.environ.copy()
env["PYTHONPATH"] = str(PYTHON_FOLDER)

scripts = sorted(
    [
        file
        for file in MODULE_PATH.glob("*.py")
        if file.name[:2].isdigit()
        and not file.name.startswith(("98", "99"))
    ]
)


with open(LOG_FILE, "w", encoding="utf-8") as log:

    log.write("="*70 + "\n")
    log.write(f"{MODULE_NAME}\n")
    log.write(f"Generated: {datetime.now()}\n")
    log.write("="*70 + "\n")


    for script in scripts:

        print(f"\nRunning {script.name}")
        log.write("="*70 + "\n")
        log.write(script.name + "\n")
        log.write("="*70 + "\n")


        result = subprocess.run(
            ["python", str(script)],
            capture_output=True,
            text=True,
            cwd=MODULE_PATH,
            env=env
        )


        log.write(result.stdout)


        if result.stderr:
            log.write("\nERROR\n")
            log.write(result.stderr)



print("\nModule Completed Successfully")
print(f"Output saved:")
print(LOG_FILE)
import argparse
import os
import sqlite3
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
PYTHON_FOLDER = PROJECT_ROOT / "python"
OUTPUT_FOLDER = PROJECT_ROOT / "outputs"
DATABASE_DIR = PROJECT_ROOT / "database"
COMMON_SQL = PROJECT_ROOT / "sql" / "common"

# These modules teach creating databases/tables, so they start with an empty DB
SELF_MANAGED = {"Module_01_Database", "Module_02_Table"}


def find_modules():
    return sorted(
        folder.name
        for folder in PYTHON_FOLDER.glob("Module_*")
        if folder.is_dir()
    )


def prepare_database(module_name):
    """Give each module its own fresh database."""
    DATABASE_DIR.mkdir(exist_ok=True)
    db_path = DATABASE_DIR / f"{module_name}.db"
    db_path.unlink(missing_ok=True)

    if module_name not in SELF_MANAGED:
        conn = sqlite3.connect(db_path)
        conn.executescript((COMMON_SQL / "schema.sql").read_text(encoding="utf-8"))
        conn.executescript((COMMON_SQL / "seed.sql").read_text(encoding="utf-8"))
        conn.close()
    return db_path


def run_module(module_name):
    """Run every numbered script in a module. Returns the number of failed scripts."""
    module_path = PYTHON_FOLDER / module_name
    output_path = OUTPUT_FOLDER / module_name
    output_path.mkdir(parents=True, exist_ok=True)
    log_file = output_path / "output.txt"

    env = os.environ.copy()
    env["PYTHONPATH"] = str(PYTHON_FOLDER)
    env["PYTHONIOENCODING"] = "utf-8"
    env["DATABASE_PATH"] = str(prepare_database(module_name))

    scripts = sorted(
        f for f in module_path.glob("*.py")
        if f.name[:2].isdigit() and not f.name.startswith(("98", "99"))
    )

    failed = 0
    with open(log_file, "w", encoding="utf-8") as log:
        log.write("=" * 70 + f"\n{module_name}\n" + "=" * 70 + "\n")

        for script in scripts:
            print(f"Running {script.name}")
            log.write("=" * 70 + f"\n{script.name}\n" + "=" * 70 + "\n")

            try:
                result = subprocess.run(
                    [sys.executable, str(script)],
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    cwd=module_path,
                    env=env,
                    timeout=60,
                )
            except subprocess.TimeoutExpired:
                failed += 1
                log.write("\nERROR: timed out after 60 seconds\n")
                continue

            log.write(result.stdout)
            if result.returncode != 0:
                failed += 1
                log.write(f"\nERROR (exit code {result.returncode})\n{result.stderr}")

    print(f"Output saved: {log_file}")
    return failed


def main():
    modules = find_modules()
    if not modules:
        sys.exit("No modules found")

    parser = argparse.ArgumentParser(description="Run SQL/Python learning modules")
    parser.add_argument("module", nargs="?", type=int, help="module number, e.g. 6")
    parser.add_argument("--all", action="store_true", help="run every module")
    args = parser.parse_args()

    if args.all:
        selected = modules
    else:
        choice = args.module
        if choice is None:
            print("\nAvailable Modules\n" + "-" * 30)
            for i, name in enumerate(modules, start=1):
                print(f"{i}. {name}")
            try:
                choice = int(input("\nSelect Module Number: "))
            except ValueError:
                sys.exit("Please enter a number.")

        if not 1 <= choice <= len(modules):
            sys.exit(f"Choose a number between 1 and {len(modules)}.")
        selected = [modules[choice - 1]]

    total_failed = sum(run_module(name) for name in selected)

    if total_failed:
        sys.exit(f"\n{total_failed} script(s) failed. Check the output logs.")
    print("\nAll scripts completed successfully.")


if __name__ == "__main__":
    main()
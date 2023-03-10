import subprocess
from pathlib import Path

from src.week02 import assets_dir
from src.week02.tests.test_lecture import script_paths


def main():
    assets_dir.mkdir(exist_ok=True)
    for script in script_paths:
        build_dir = assets_dir.joinpath(Path(script).stem)
        subprocess.run(f"eopsin build {script} -o {build_dir}".split())


if __name__ == "__main__":
    main()

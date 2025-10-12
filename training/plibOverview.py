from pathlib import Path
import argparse


def main():
    parser = argparse.ArgumentParser(description='Plib Overview')
    parser.add_argument('--file', required=True, help='Path to the folder')
    args = parser.parse_args()
    filename = Path(args.file)
    print(Path.cwd())
    path = Path.cwd() / "projectstructure.md"
    with path.open() as f:
        print(f.read())
    pathr = Path("plibOverview.py")
    print(pathr.resolve())
    print(pathr.stem)
    print(path.is_dir())
    print("")
    with filename.open("r") as f:
        print(f.read())


if __name__ == '__main__':
    main()

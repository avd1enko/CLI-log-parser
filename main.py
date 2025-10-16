from analyzer import *
from parser import *
import pathlib

def main(path: str):
    path = pathlib.Path(path)
    with path.open("r") as f:
        for line in f:
            line = f.readline()
            result = parse(line)
            print(error_analyzer(result))

if __name__ == "__main__":
    main("/Users/danilaavdienko/Desktop/logLibrary/site1.log")
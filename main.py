from analyzer import error_log, get_method_log, post_method_log, path_heatmap_log
from parser import parse
import pathlib

def main(path: str):
    path = pathlib.Path(path)
    log_entries = []
    print(f"{"TIME":<30} | {"IP":<15} | {"METHOD":<9} | {"PATH":<17} | {"STATUS":<9} | {"SIZE":<9}\n{'-' * 100}")
    with path.open("r") as f:
        for line in f:
            log_entry = parse(line.strip())
            if log_entry:
                log_entries.append(log_entry)
    print(*error_log(log_entries), sep="\n")
    print(*get_method_log(log_entries), sep="\n")
    print(*post_method_log(log_entries), sep="\n")
    for key, value in path_heatmap_log(log_entries).items():
        print(f"{key:<30} | {value:<15}")




if __name__ == "__main__":
    main("/Users/danilaavdienko/Desktop/logLibrary/site1.log")
from analyzer import error_log, method_log, path_heatmap_log
from parser import parse_log
from argparser import get_args
import pathlib


def main():
    args = get_args()
    path = pathlib.Path(args.logfilePath)
    log_entries = []
    with path.open("r") as f:
        for line in f:
            log_entry = parse_log(line.strip())
            if log_entry:
                log_entries.append(log_entry)
    if args.error:
        print(f"{"TIME":<30} | {"IP":<15} | {"METHOD":<9} | {"PATH":<17} | {"STATUS":<9} | {"SIZE":<9}\n{'-' * 100}")
        print(*error_log(log_entries), sep="\n")
    if args.method:
        print(f"{"TIME":<30} | {"IP":<15} | {"METHOD":<9} | {"PATH":<17} | {"STATUS":<9} | {"SIZE":<9}\n{'-' * 100}")
        for i in args.method:
            print(*method_log(log_entries, method=i), sep="\n")
    if args.pathHM:
        print(f"{"PATH":<30} | {"VISITED":<15}")
        for key, value in path_heatmap_log(log_entries).items():
            print(f"{key:<30} | {value:<15}")




if __name__ == "__main__":
    main()
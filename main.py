from src.analyzer import error_log, method_log, path_heatmap_log
from src.parser import parse_log
from src.argparser import get_args
import pathlib


def main():
    args = get_args()
    # weak multi_args logic, must rework!
    if args.multiArgs:
        multiAtgs = [arg for arg in args.multiArgs.split("+") if args.multiArgs]
    else:
        multiAtgs = None
    path = pathlib.Path(args.logfilePath)
    log_entries = []
    with path.open("r") as f:
        for line in f:
            log_entry = parse_log(line.strip())
            if log_entry:
                log_entries.append(log_entry)
    #weak logic, must rework!
    if multiAtgs:
        inner_log_entries = log_entries
        for i in multiAtgs:
            match i:
                case "error":
                    inner_log_entries = error_log(inner_log_entries)
                case "POST":
                    inner_log_entries = method_log(inner_log_entries, "POST")
                case "GET":
                    inner_log_entries = method_log(inner_log_entries, "GET")
        print(*inner_log_entries, sep="\n")


    if args.error:
        print(f"{"TIME":<30} | {"IP":<15} | {"METHOD":<9} | {"PATH":<17} | {"STATUS":<9} | {"SIZE":<9}\n{'-' * 100}")
        print(*error_log(log_entries), sep="\n")
    if args.method:
        print(f"{"TIME":<30} | {"IP":<15} | {"METHOD":<9} | {"PATH":<17} | {"STATUS":<9} | {"SIZE":<9}\n{'-' * 100}")
        for i in args.method:
            print(*method_log(log_entries, method=i), sep="\n")
    if args.pathHM:
        print(f"{"PATH":<30} | {"VISITED":<15}")
        for key, value in dict(sorted(path_heatmap_log(log_entries).items(), key=lambda item: item[1])).items():
            print(f"{key:<30} | {value:<15}")




if __name__ == "__main__":
    main()
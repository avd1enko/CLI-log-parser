from pathlib import Path
from src.analyzer import error_log, method_log, path_heatmap_log
from src.parser import parse_log
from src.argparser import get_args


def print_log_table(entries):
    print(f"{'TIME':<30} | {'IP':<15} | {'METHOD':<9} | {'PATH':<17} | {'STATUS':<9} | {'SIZE':<9}")
    print('-' * 100)
    print(*entries, sep="\n")


def print_path_heatmap(entries):
    print(f"{'PATH':<30} | {'VISITED':<15}")
    for key, value in dict(sorted(path_heatmap_log(entries).items(), key=lambda item: item[1])).items():
        print(f"{key:<30} | {value:<15}")


def apply_multi_args(log_entries, multi_args_raw):
    multi_args = multi_args_raw.split("+") if multi_args_raw else []
    if not multi_args:
        return None

    filtered = log_entries

    if "error" in multi_args:
        filtered = error_log(filtered)

    method = next((m for m in ("GET", "POST") if m in multi_args), None)
    if method:
        filtered = method_log(filtered, method)

    if "pathHM" in multi_args:
        print_path_heatmap(filtered)
        return None

    return filtered


def main():
    args = get_args()
    path = Path(args.logfilePath)
    log_entries = []

    with path.open("r") as f:
        for line in f:
            log_entry = parse_log(line.strip())
            if log_entry:
                log_entries.append(log_entry)

    # multiArgs
    filtered = apply_multi_args(log_entries, args.multiArgs)
    if filtered is not None:
        print_log_table(filtered)
        return

    # single flags
    if args.error:
        print_log_table(error_log(log_entries))

    if args.method:
        for method in args.method:
            print_log_table(method_log(log_entries, method))

    if args.pathHM:
        print_path_heatmap(log_entries)


if __name__ == "__main__":
    main()
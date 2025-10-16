import json
from log_enrty import LogEntry


def error_log(list_log_entry: list[LogEntry]):
    return [entry for entry in list_log_entry if entry.is_error()]


def method_log(list_log_entry: list[LogEntry], method: str):
    return [entry for entry in list_log_entry if entry.method == method]


def path_heatmap_log(list_log_entry: list[LogEntry]):
    pathes = {}
    for entry in list_log_entry:
        pathes[entry.path] = pathes.get(entry.path, 0) + 1
    return pathes



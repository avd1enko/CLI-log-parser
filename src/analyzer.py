import json
from .log_entry import LogEntry


def error_log(list_log_entry: list[LogEntry]):
    """Returns a list of log entries that have error status codes (4xx or 5xx)"""
    return [entry for entry in list_log_entry if entry.is_error()]


def method_log(list_log_entry: list[LogEntry], method: str):
    """Returns a list of log entries that have specific HTTP method (GET or POST)"""
    return [entry for entry in list_log_entry if entry.method == method]


def path_heatmap_log(list_log_entry: list[LogEntry]):
    """Return a dict {path:times_visited}"""
    pathes = {}
    for entry in list_log_entry:
        pathes[entry.path] = pathes.get(entry.path, 0) + 1
    return pathes



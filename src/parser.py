from .log_entry import LogEntry
import re


def parse_log(line: str):
    """Parses a log line and returns a LogEntry object, or None if parsing fails."""
    pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<time>.*?)] "(?P<method>\w+) (?P<path>.*?) HTTP/1.1" (?P<status>\d+) (?P<size>\d+) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"')
    match = pattern.match(line)
    if not match:
        return None
    return LogEntry(ip=match.group("ip"),
                    time=match.group("time"),
                    method=match.group("method"),
                    path=match.group("path"),
                    status=match.group("status"),
                    size=match.group("size"),
                    referrer=match.group("referrer"),
                    user_agent=match.group("user_agent"))

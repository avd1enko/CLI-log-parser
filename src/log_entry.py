class LogEntry:
    """Represents a single log entry as an object with its own attributes and methods."""
    def __init__(self, ip, time, method, path, status, size, referrer, user_agent):
        self.ip = ip
        self.time = time
        self.method = method
        self.path = path
        self.status = status
        self.size = size
        self.referrer = referrer
        self.user_agent = user_agent

    def __str__(self):
        return f"{self.time:<30} | {self.ip:<15} | {self.method:<9} | {self.path:<17} | {self.status:<9} | {self.size:<9}\n{'-' * 100}"

    def is_error(self) -> bool:
        return self.status[0] in {"4", "5"}


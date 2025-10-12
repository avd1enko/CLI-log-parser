import re
def main():
    pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<time>.*?)] "(?P<method>\w+) (?P<path>.*?) HTTP/1.1" (?P<status>\d+) (?P<size>\d+) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"')
    line = '192.168.1.69 - - [12/Oct/2025:16:26:07 +0000] "GET /login HTTP/1.1" 400 216 "-" "curl/7.68.0"'
    match = pattern.match(line)
    return {"ip": match.group("ip"), "time": match.group("time"), "method":match.group("method"),
            "path":match.group("path"), "status":match.group("status"), "size":match.group("size"),
            "referrer":match.group("referrer"), "user_agent":match.group("user_agent")}

if __name__ == "__main__":
    main()
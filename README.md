# CLI Log Analyzer for Nginx Access Logs

Welcome!  
This is my pet-project — a simple and extensible command-line tool for analyzing Nginx Access logs. It supports filtering by HTTP method, detecting errors, generating path heatmaps,   and combining multiple filters through the CLI interface (**more to come!**).

## Installation

```bash
git clone https://github.com/avd1enko/CLI-log-parser
python3 -m venv venv
source venv/bin/activate
```

---

## Usage

```bash
python main.py path/to/logfile.log [options]
```

### Required argument:
- `logfilePath` — path to the `.log` file to analyze.

---

### Optional arguments:

| Argument             | Description                                                                                       |
|----------------------|---------------------------------------------------------------------------------------------------|
| `--error`            | Shows all requests that resulted in error responses (4xx or 5xx).                                 |
| `--method GET POST`  | Shows all requests matching the specified HTTP methods (supports multiple values).                |
| `--pathHM`           | Displays a heatmap of paths showing how many times each path was requested.                      |
| `--multiArgs`        | Combines filters. Example: `--multiArgs error+POST` → shows only POST requests with errors.       |
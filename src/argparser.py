def get_args():
    import argparse
    parser = argparse.ArgumentParser(description="CLI tool for analyzing nginx log files")

    parser.add_argument(
        "logfilePath",
        type=str,
        help="Path to the log file to analyze"
    )

    parser.add_argument(
        "--multiArgs",
        type=str,
        help="Combine multiple filters (e.g. error+POST) to show only entries that match both criteria"
    )

    parser.add_argument(
        "--method",
        nargs="+",
        choices=["GET", "POST"],
        help="Filter entries by HTTP method (GET or POST)"
    )

    parser.add_argument(
        "--error",
        action="store_true",
        help="Show only entries with error status codes (4xx and 5xx)"
    )

    parser.add_argument(
        "--pathHM",
        action="store_true",
        help="Display a heatmap of request paths with visit counts"
    )

    return parser.parse_args()
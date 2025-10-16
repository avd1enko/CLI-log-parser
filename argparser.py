def get_args():
    import argparse
    parser = argparse.ArgumentParser(description="CLI nginx log analyzer")

    parser.add_argument("logfilePath", type=str, help="Path to the log file")
    parser.add_argument("--method", nargs="+", choices=["GET", "POST"], help="Method")
    parser.add_argument("--error", action="store_true", help="Error logs")
    parser.add_argument("--pathHM", action="store_true", help="Path heatmap logs")

    return parser.parse_args()
